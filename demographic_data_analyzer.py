import pandas as pd

def calculate_demographic_data():
    # Lire et préparer les données
    df = pd.read_csv("data.csv", sep=';', skiprows=1)
    df.columns = df.columns.str.strip()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.drop(columns=df.columns[0])  # Supprimer colonne vide

    # 1. Nombre de personnes par race
    race_count = df['race'].value_counts()

    # 2. Âge moyen des hommes
    average_age_men = round(df[df['sex'] == 'Male']['age'].astype(float).mean(), 1)

    # 3. Pourcentage de personnes avec un diplôme Bachelor
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Pourcentage de riches selon niveau d'étude
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_edu_rich = df[higher_education & (df['salary'] == '>50K')]
    lower_edu_rich = df[lower_education & (df['salary'] == '>50K')]

    higher_education_rich = round((len(higher_edu_rich) / higher_education.sum()) * 100, 1)
    lower_education_rich = round((len(lower_edu_rich) / lower_education.sum()) * 100, 1)

    # 5. Heures de travail minimum
    min_work_hours = int(df['hours-per-week'].astype(float).min())

    # 6. % des personnes avec min d’heures qui gagnent >50K
    min_workers = df[df['hours-per-week'].astype(float) == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round(len(rich_min_workers) / len(min_workers) * 100, 1)

    # 7. Pays avec le pourcentage le plus élevé de >50K
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_by_country = df['native-country'].value_counts()
    rich_country_ratio = (rich_by_country / total_by_country).fillna(0)
    highest_earning_country = rich_country_ratio.idxmax()
    highest_earning_country_percentage = round(rich_country_ratio.max() * 100, 1)

    # 8. Profession la plus populaire pour >50K en Inde
    india_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_occupations['occupation'].value_counts().idxmax() if not india_occupations.empty else "N/A"

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
