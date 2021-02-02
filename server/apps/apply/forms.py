from django import forms
from .models import ApplyForm, ApplyConfig


class ApplicationForm(forms.ModelForm):
    def clean(self):
        raw_data = self.data
        interview_date = list()
        interview_len_1 = int(self.data.get("interview_list_len_2"))
        interview_len_2 = int(self.data.get("interview_list_len_2"))
        for i in range(interview_len_1):
            for j in range(interview_len_2):
                val = raw_data.get("date_%d_%d" % (i, j))
                if val == "1":
                    interview_date.append(val)
                else:
                    interview_date.append("0")

        self.cleaned_data["interview_date"] = ",".join(interview_date)
        return self.cleaned_data

    class Meta:
        model = ApplyForm
        exclude = ['user']
