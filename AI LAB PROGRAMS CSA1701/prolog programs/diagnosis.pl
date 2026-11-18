
symptom(fever, flu).
symptom(cough, flu).
symptom(body_pain, flu).

symptom(sneezing, cold).
symptom(runny_nose, cold).
symptom(cough, cold).

symptom(headache, migraine).
symptom(nausea, migraine).

diagnosis(Patient, Disease) :-
    has_symptom(Patient, Symptom),
    symptom(Symptom, Disease).

has_symptom(shaik, fever).
has_symptom(shaik, cough).
has_symptom(shaik, body_pain).
