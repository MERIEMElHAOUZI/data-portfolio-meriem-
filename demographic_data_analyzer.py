import pandas as pd

def calculate_demographic_data():
    # Lire et préparer les données
    df = pd.read_csv("data.txt", sep='|', skipinitialspace=True)
    df.columns = df.columns.str.strip()  # Nettoyage des noms de colonnes

    # 1. Combien de personnes de chaque race ?
    race_count = df['race'].value_counts()

    # 2. Âge moyen des hommes
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Pourcentage de personnes avec un diplôme Bachelor
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. % avec un diplôme avancé (Bachelors, Masters, Doctorate) et >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = df[higher_education & (df['salary'] == '>50K')]
    lower_education = ~higher_education
    lower_edu_rich = df[lower_education & (df['salary'] == '>50K')]

    if higher_education.sum() > 0:
      higher_education_rich = round((len(higher_edu_rich) / higher_education.sum()) * 100, 1)
    else:
       higher_education_rich = 0.0  # Aucun diplômé, donc 0%

    if lower_education.sum() > 0:
       lower_education_rich = round((len(lower_edu_rich) / lower_education.sum()) * 100, 1)
    else:
      lower_education_rich = 0.0  # Aucun non-diplômé, donc 0%

    lower_education_rich = round((len(lower_edu_rich) / lower_education.sum()) * 100, 1)

    # 5. Heures de travail minimum
    min_work_hours = df['hours-per-week'].min()

    # 6. % des personnes avec min de travail qui gagnent >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round(len(rich_min_workers) / len(min_workers) * 100, 1)

       # 7. Pays avec le plus haut % de >50K
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_by_country = df['native-country'].value_counts()
    rich_country_ratio = (rich_by_country / total_by_country).fillna(0)
    highest_earning_country = rich_country_ratio.idxmax()
    highest_earning_country_percentage = round(rich_country_ratio.max() * 100, 1)

    # 8. Profession la plus populaire pour >50K en Inde
    india_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not india_occupations.empty:
        top_IN_occupation = india_occupations['occupation'].value_counts().idxmax()
    else:
        top_IN_occupation = "N/A"


    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
