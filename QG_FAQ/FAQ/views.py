from django.shortcuts import render
import csv
from FAQ.models import Questions


def FAQ_page(request):
    if request.method == "GET":
        questions = Questions.objects.all()
        return render(request, '../templates/FAQ_page.html', {
            "questions": questions,
        })

    else:
        f = request.FILES['file']
        print(f)
        file_path = 'FAQ/data/' + f.name
        with open(file_path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        datas = read_from_tsv(file_path, ['answer_text', 'question_text'])
        for data in datas:
            answer_text = data['answer_text']
            question_text = data['question_text']
            Questions.objects.create(question_text=question_text, answer_text=answer_text)
        questions = Questions.objects.all()
        return render(request, '../templates/FAQ_page.html', {
            'file': f,
            "questions": questions,
        })


def write_to_tsv(output_path: str, file_columns: list, data: list):
    csv.register_dialect('tsv_dialect', delimiter='\t', quoting=csv.QUOTE_ALL)
    with open(output_path, "w", newline="") as wf:
        writer = csv.DictWriter(wf, fieldnames=file_columns, dialect='tsv_dialect')
        writer.writerows(data)
        csv.unregister_dialect('tsv_dialect')


def read_from_tsv(file_path: str, column_names: list) -> list:
    csv.register_dialect('tsv_dialect', delimiter='\t', quoting=csv.QUOTE_ALL)
    with open(file_path, "r") as wf:
        reader = csv.DictReader(wf, fieldnames=column_names, dialect='tsv_dialect')
        datas = []
        for row in reader:
            data = dict(row)
            datas.append(data)
        csv.unregister_dialect('tsv_dialect')
    return datas


# def upload(request):
#     file = request.FILES['file']
#     file_name = file.name
#     file_path = 'FAQ/data/' + file_name
#     file.save(file_path)
#
#     return render(request, '../templates/FAQ_page.html', {'file_name': file_name})
