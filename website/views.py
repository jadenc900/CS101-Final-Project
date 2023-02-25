from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Comments
from .models import Notifications
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST', 'NOTIFICATION'])
@login_required
def home():
#    if request.method == 'POST': 
#        comment = request.form.get('comment')#Gets the comment from the HTML 

#        if len(comment) < 1:
#            flash('Comment is too short!', category='error') 
#       else:
#            new_comment = Comment(data=comment, user_id=current_user.id)  #providing the schema for the comment
#            db.session.add(new_comment) #adding the note to the database 
#            db.session.commit()
#            flash('Comment added!', category='success')

    return render_template("mainpage.html", user=current_user)


#@views.route('/delete-note', methods=['POST'])
#def delete_note():  
##    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
#    noteId = note['noteId']
#    note = Note.query.get(noteId)
#    if note:
#        if note.user_id == current_user.id:
# #          db.session.delete(note)
#            db.session.commit()
#
#    return jsonify({})
