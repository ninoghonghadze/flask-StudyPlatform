from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
import os
from .models import Material, Note, Reply
from . import db

views = Blueprint('views', __name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note_data = request.form.get('note')

        if len(note_data) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note_data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully!', category='success')

    notes = Note.query.filter_by(user_id=current_user.id).all()
    unsatisfied_count = Note.query.filter_by(user_id=current_user.id, satisfied=False).count()

    return render_template("home.html", user=current_user, notes=notes, unsatisfied_count=unsatisfied_count)

@views.route('/delete-note/<int:id>', methods=['POST'])
@login_required
def delete_note(id):
    note = Note.query.get_or_404(id)

    if note.user_id != current_user.id:
        flash('Unauthorized action!', category='error')
        return redirect(url_for('views.home'))

    db.session.delete(note)
    db.session.commit()
    flash('Note deleted successfully!', category='success')

    return redirect(url_for('views.home'))

@views.route('/edit-note/<int:id>', methods=['POST'])
@login_required
def edit_note(id):
    note = Note.query.get_or_404(id)

    if note.user_id != current_user.id:
        flash('Unauthorized action!', category='error')
        return redirect(url_for('views.home'))

    new_data = request.form.get('new_data')

    if new_data:
        note.data = new_data
        db.session.commit()
        flash('Note edited successfully!', category='success')

    return redirect(url_for('views.home'))

@views.route('/reply/<int:note_id>', methods=['POST'])
@login_required
def reply(note_id):
    reply_text = request.form.get('reply_text')
    if reply_text:
        note = Note.query.get_or_404(note_id)
        new_reply = Reply(content=reply_text, note=note)
        db.session.add(new_reply)
        db.session.commit()
        flash("Reply added!", category="success")
    return redirect(url_for('views.home'))

@views.route('/done/<int:note_id>', methods=['POST'])
@login_required
def done(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    flash("Note marked as done and removed.", category="success")
    return redirect(url_for('views.home'))

@views.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        category = request.form.get('category')

        if not file:
            flash('No file selected.', category='error')
            return redirect(url_for('views.upload'))

        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        try:
            file.save(filepath)
            new_material = Material(filename=filename, category=category, user_id=current_user.id)
            db.session.add(new_material)
            db.session.commit()
            flash('File uploaded successfully!', category='success')
            return redirect(url_for('views.materials'))
        except Exception as e:
            flash(f'Error uploading file: {str(e)}', category='error')
            return redirect(url_for('views.upload'))

    return render_template("upload.html", user=current_user)

@views.route('/materials')
@login_required
def materials():
    materials = Material.query.all()
    return render_template("materials.html", materials=materials, user=current_user)

