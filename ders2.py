#Ö1

employees = [
    {"name": "Ahmet", "department": "IT", "projects": [{"name": "CRM", "completed": True, "hours": 120}, {"name": "Security", "completed": False, "hours": 80}]},
    {"name": "Elif", "department": "HR", "projects": [{"name": "Hiring System", "completed": True, "hours": 90}, {"name": "Employee Portal", "completed": True, "hours": 100}]},
    {"name": "Mehmet", "department": "IT", "projects": [{"name": "Cloud Migration", "completed": True, "hours": 150}, {"name": "Data Analysis", "completed": True, "hours": 130}]},
    {"name": "Ayşe", "department": "Marketing", "projects": [{"name": "Social Media", "completed": True, "hours": 60}, {"name": "SEO", "completed": False, "hours": 50}]}
]
""" Yapılması Gerekenler:
En çok saat harcayan çalışanı bulun.
Tamamlanan proje sayısı en yüksek olan çalışanı belirleyin.
Her departmandaki toplam çalışma saatlerini hesaplayın.
En çok proje yapan departmanı bulun.
Tüm projelerin tamamlanma yüzdesini hesaplayın."""

#soru 1
encokcalisan= employees[0]
enazcalisan= employees[0]
for n in employees:
  if enazcalisan["projects"][0]["hours"] > n["projects"][0]["hours"]:
    enazcalisan = n
  if encokcalisan["projects"][0]["hours"] < n["projects"][0]["hours"]:
    encokcalisan = n

print(encokcalisan["name"])
print(enazcalisan["name"])

#soru 2

tamamlananprojesayisi = []

for i in employees:
  tamamlananproje = 0
  for j in i["projects"]:
    if j["completed"] == True:
      tamamlananproje += 1
  tamamlananprojesayisi.append(tamamlananproje)

isimliliste = list(zip(tamamlananprojesayisi, employees))

enfazlabitiren= isimliliste[0]
enazbitiren= isimliliste[0]
for n in isimliliste:
  if enazbitiren[0] > n[0]:  
    enazbitiren = n
    
  if enfazlabitiren[0] < n[0]: 
    enfazlabitiren = n

print(enfazlabitiren[1]["name"]) 
print(enazbitiren[1]["name"])

#soru 3
#toplam 3 farklı departman var. IT, HR, Marketing

calisilansaatler = []

for i in employees:
    toplam_saat = 0  
    for j in i["projects"]:
        toplam_saat += j["hours"] 
    calisilansaatler.append((i["department"], toplam_saat))

departmansaatleri = {}

for departman, hours in calisilansaatler:
    if departman not in departmansaatleri:
        departmansaatleri[departman] = 0
    departmansaatleri[departman] += hours

for departman, total_hours in departmansaatleri.items():
    print(f"{departman} departmanında toplam {total_hours} saat çalışılmıştır.")

#soru 4
tamamlananprojesayisi = []

for i in employees:
    tamamlananproje = 0
    for j in i["projects"]:
        if j["completed"] == True:
            tamamlananproje += 1
    tamamlananprojesayisi.append((i["department"], tamamlananproje))

departmantoplamları = {}

for departman, sayi in tamamlananprojesayisi:
    if departman not in departmantoplamları:
        departmantoplamları[departman] = 0
    departmantoplamları[departman] += sayi

for departman, toplam in departmantoplamları.items():
    print(f"{departman} departmanı toplamda {toplam} proje bitirmiştir.")

max_department = max(departmantoplamları, key=departmantoplamları.get)
print(f"\nEn çok proje yapan departman: {max_department} ({departmantoplamları[max_department]} proje)")

#soru5

BitmişProjeyeHarcananSure = 0
ToplamHarcananSure = 0

for i in employees:
    for j in i["projects"]:
        ToplamHarcananSure += j["hours"] 
        if j["completed"]:
            BitmişProjeyeHarcananSure += j["hours"]

tamamlanmayuzdesi = (BitmişProjeyeHarcananSure / ToplamHarcananSure) * 100 

print(f"Tüm projelerin tamamlanma yüzdesi: %{tamamlanmayuzdesi}")