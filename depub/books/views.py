from django.shortcuts import render

# Create your views here.
class Create(LoginRequiredMixin, View):
    template = 'recipes/partials/create_update.html'

    def get(self, request):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe_form = RecipeForm()
        ingredient_formset = RecipeIngredientFormSet()
        context = {
            'recipe_form': recipe_form,
            'ingredient_formset': ingredient_formset,
            'base_template': base_template,
        }
        return render(request, self.template, context)

    @transaction.atomic
    def post(self, request):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe_form = RecipeForm(request.POST)
        ingredient_formset = RecipeIngredientFormSet(request.POST)
        # validar os formularios
        if any(
                [
                    not recipe_form.is_valid(),
                    not ingredient_formset.is_valid(),
                ]
        ):
            # Nao passou na validacao, retorna o form com o erro.
            context = {
                'recipe_form': recipe_form,
                'ingredient_formset': ingredient_formset,
                'base_template': base_template,
            }
            return render(request, self.template, context, status=400)

        # salva os formularios
        recipe_form.instance.created_by = request.user
        recipe = recipe_form.save()
        for form in ingredient_formset:
            if form.has_changed():
                form.instance.recipe = recipe
                form.save()

        # reset forms
        recipe_form = RecipeForm()
        ingredient_formset = RecipeIngredientFormSet()
        context = {
            'recipe_form': recipe_form,
            'ingredient_formset': ingredient_formset,
            'base_template': base_template,
        }
        messages.success(request, 'Receita criada.')
        return render(request, self.template, context, status=201)

