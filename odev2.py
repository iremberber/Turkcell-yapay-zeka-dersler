baseUrl_category = "http://localhost:3000/categories"
baseUrl_course= "http://localhost:3000/courses"
baseUrl_lesson= "http://localhost:3000/lessons"
baseUrl_student= "http://localhost:3000/students"
baseUrl_enrollments="http://localhost:3000/enrollments"
baseUrl_payments="http://localhost:3000/payments"

import requests

#CATEGORY

#Category listelemek için;
"""def getCategory():
    response =  requests.get(baseUrl_category)
    return response.json()

for product in getCategory():
    print(product.get("name"), "/",product.get("description"))"""

#Category eklemek için fakat aynı isimde bir kategori varsa hata döndürecek şekilde;

"""def createCategory(category):
    existing_categories = requests.get(baseUrl_category).json()
    
    for categories in existing_categories:
        if categories["name"] == category["name"]:
            return {"error": "Bu kategori adı zaten mevcut!"}
        
    response = requests.post(baseUrl_category, json=category)
    return response.json()
    
new_category = {"id": 5, "name": "Veri Bilimi", "description": "Veri analizi ve makine öğrenmesi"}
print(createCategory(new_category))"""

#Category i güncellemek için;

"""def updateCategory(id, category):
    response = requests.put(baseUrl_category + "/" + str(id), json=category)
    return response.json()

categoryToUpdate = {
    "id": 999,  
    "name": "yeniCategory",
    "description": "yeni aciklama"
}

print(updateCategory(5, categoryToUpdate)) """

#Category silmek için;

"""def deleteCategoryById(id):
    response = requests.delete(baseUrl_category+"/"+str(id))
    return response.json()

deleteCategoryById("5")"""

#COURSE

#Course listelemek için;
"""def getCourseByTitle(title):
    response = requests.get(baseUrl_course+"/?title="+str(title))
    return response.json()

for  titles in getCourseByTitle("Django ile Web Geliştirme"):
    print(titles.get("title"), "/",titles.get("price"),"/",titles.get("id"))"""

#Course create etmek için fakat önce kategori id kontrolü yapıyor ve yayınlanmayı girişte direkt false yapıyor. Daha sonra yayınlamak için publishCourse fonksiyonu ile yayınlanıyor;

"""def createCourse(course):
    categories = requests.get(baseUrl_category).json() 
    category_ids = [int(category["id"]) for category in categories]

    if int(course["category_id"]) not in category_ids:
        return {"error": "Geçersiz kategori ID!"}
    
    course["is_published"] = False
    response = requests.post(baseUrl_course, json=course)
    return response.json()

CourseToCreate = {
      "id": "999",
      "title": "ileri düzey Django ile Web Geliştirme ",
      "description": "ileri düzey Python ile web geliştirme",
      "category_id": 6,
      "price": 150,
      "created_at": "2024-03-11"}
print(createCourse(CourseToCreate))

def publishCourse(id):
    response = requests.get(baseUrl_course + "/" + str(id))
    
    if response.status_code != 200:
        return {"error": "Kurs bulunamadı!"}

    course = response.json()
    course["is_published"] = True

    response = requests.put(baseUrl_course + "/" + str(id), json=course)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Kurs güncellenemedi!", "details": response.json()}

print(publishCourse(6)) """

#Course güncellemek için;

"""def updateCourse(id, course):
    response = requests.put(baseUrl_course + "/" + str(id), json=course)
    return response.json()

courseToUpdate = {
    "title": "Çok çok ileri düzey Django ile Web Geliştirme ",
    "description": "Çok çok ileri düzey Python ile web geliştirme"
}

print(updateCourse(999, courseToUpdate))""" 

#Course silmek için;

"""def deleteCourseById(id):
    response = requests.delete(baseUrl_course+"/"+str(id))
    return response.json()

deleteCourseById("999") """

#LESSON

#Lesson listelemek için ama course_id sine göre;

"""def getLessonByCourse(course_id):
    response = requests.get(baseUrl_lesson+"/?course_id="+str(course_id))
    return response.json()

for  lessons in getLessonByCourse("6"):
    print(lessons.get("title"), "/",lessons.get("content"),"/",lessons.get("course_id"))"""

#Lesson create etmek için;

"""def createLesson(lesson):
    response = requests.post(baseUrl_lesson,json=lesson)
    return response.json()

createToLesson = {"id": 4, "title": "HTML & CSS Temelleri",
                    "content": "Web geliştirme için HTML ve CSS'in temelleri",
                    "video_url": "https://example.com/video4", "course_id": 4}
createLesson(createToLesson)"""

#Lesson güncellemek için;

"""def updateLesson(id, lesson):
    response = requests.put(baseUrl_lesson + "/" + str(id), json=lesson)
    return response.json()

lessonToUpdate = {
    "title": "ileri düzey HTML & CSS Temelleri",
    "content": "ileri düzey Web geliştirme için HTML ve CSS'in temelleri",
}

print(updateLesson(4, lessonToUpdate))"""

#Lesson silmek için;

"""def deleteLessonById(id):
    response = requests.delete(baseUrl_lesson+"/"+str(id))
    return response.json()

deleteLessonById("4")"""

#STUDENT

#Student listelemek için;
"""def getStudent():
    response =  requests.get(baseUrl_student)
    return response.json()

for product in getStudent():
    print(product.get("name"), "/",product.get("email"))"""

#Email ile öğrenci getirmek için;

"""def getstudentByEmail(email):
    response = requests.get(baseUrl_student+"/?email="+str(email))
    return response.json()

for  students in getstudentByEmail("gamze@example.com"):
    print(students.get("id"), "/",students.get("name"),"/",students.get("password"))"""

#Student create etmek için;

"""def createStudent(Student):
    response = requests.post(baseUrl_student,json=Student)
    return response.json()

createToStudent = {      
        "id": "888",
        "name": "İrem Berber",
        "email": "irem@example.com",
        "password": "b2a5f64e1"}
createStudent(createToStudent)"""

#Student güncellemek için;

"""def updateStudent(id, student):
    response = requests.put(baseUrl_student + "/" + str(id), json=student)
    return response.json()

studentToUpdate = {
      "email": "silinecek@example.com",
      "password": "b2a5f64e16e5387b33900b4bdcc276bc"}

print(updateStudent(888, studentToUpdate))"""

#Student silmek için;  

"""def deleteStudentById(id):
    response = requests.delete(baseUrl_student+"/"+str(id))
    return response.json()

deleteStudentById("888")"""

#Öğrenci Login işlemi için;

"""def loginStudent(email, password):
    students = requests.get(baseUrl_student).json()
    
    student = None
    for s in students:
        if s['email'] == email:
            student = s
            break  
    
    if student:
        if student['password'] == password:
            return {"message": "Giriş başarılı!"}
        else:
            return {"error": "Şifre yanlış!"}
    else:
        return {"error": "Öğrenci bulunamadı!"}
    
print(loginStudent("zeynep@example.com", "3f786850e387550fdab836ed7e6dc881de23001b"))"""

#kurslara kayıt olmak için;

"""def enrollStudentToCourse(student_id, course_id):
    response = requests.post(baseUrl_enrollments, json={"student_id": student_id, "course_id": course_id})
    return response.json()

print(enrollStudentToCourse(1, 5))""" #oluşan ID'yi sistem kafadan uyduruyor.


#ödemeler yapılmış mı? sorgusu diyerek anladım

"""def isPaymentDone(student_id, course_id):
    response = requests.get(baseUrl_payments+"/?student_id="+str(student_id)+"&course_id="+str(course_id))
    return response.json()

for payments in isPaymentDone(5, 5):
    print("Student Id'si ",payments.get("student_id"),"olan şahısın ödeme durumu",payments.get("status"))"""