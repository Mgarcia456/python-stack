from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.recipe import Recipe

#### create page rendering a template
@app.route('/recipes/new')
def new_recipe():
    return render_template('recipe_new.html')
## create a recipe
@app.route('/recipes/create',methods=['post'])
def create_recipe():
    print(request.form)
    if not Recipe.vaildator(request.form):
        return redirect('/recipes/new')
    # else create recipe
    recipe_data = {
        **request.form,
        'user_id' : session['user_id']
    }
    Recipe.create(recipe_data)
    return redirect('/dashboard')
#    show one
@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    recipe_data = {
          'id' : id
    }
    this_recipe = Recipe.get_by_id(recipe_data)
    return render_template("recipe_show.html",this_recipe=this_recipe)
#     edit page render
@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    this_recipe = Recipe.get_by_id({'id':id})
    return render_template('recipe_edit.html', this_recipe=this_recipe)
#    edit page action
@app.route('/recipes/<int:id>/update', methods=['post'])
def update_recipe(id):
    if not Recipe.vaildator(request.form):
        return redirect(f'/recipes/{id}/edit')
    
    update_data = {
        **request.form,
        'id' : id
    }
    Recipe.update(update_data)
    return redirect('/dashboard')
############   delete 
@app.route('/recipes/<int:id>/delete')
def delete(id):
    
    Recipe.delete({'id' : id})
    return redirect("/dashboard")