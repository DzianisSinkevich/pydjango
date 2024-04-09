from django.shortcuts import render, redirect
from .models import FinData, Category, FinDataGroup
from .forms import FinDataForm
from django_pandas.io import read_frame
import pandas as pd


def from_db_to_pandas(dataset):
    df = pd.DataFrame()
    df = read_frame(dataset)

    df = df.groupby(['category', 'operation'])['value'].sum().sort_values(ascending=False).reset_index(name="value")
    dft = pd.DataFrame(df)
    return dft


def delete_findatagroup(self):
    FinDataGroup.objects.all().delete()


def findata_home(request):
    fin_data = FinData.objects.order_by('date')
    categories = Category.objects.all()
    form = FinDataForm()

    df = from_db_to_pandas(fin_data)

    delete_findatagroup(FinDataGroup)

    for row in df.iterrows():
        FinDataGroup.objects.create(
            category=row[1].iloc[0],
            value=row[1].iloc[2],
            operation=row[1].iloc[1],
            date_me="01-01-2024"
        )

    fin_data_group_income = FinDataGroup.objects.filter(operation='Доход').values()
    fin_data_group_expenses = FinDataGroup.objects.filter(operation='Расход').values()

    error = ''
    if request.method == 'POST':
        form = FinDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('findata_home')
        else:
            error = 'Некорректные данные'

    return render(request, 'findata/findata_home.html',
                  {'fin_data': fin_data,
                   'categories': categories,
                   'form': form,
                   'error': error,
                   'fin_data_group_income': fin_data_group_income,
                   'fin_data_group_expenses': fin_data_group_expenses})


def findata_statistic(request):
    return render(request, "findata/findata_statistic.html")
