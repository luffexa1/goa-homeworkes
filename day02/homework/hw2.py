#(bonus - აუცილებელი არაა ამის გაკეთება, უბრალოდ ვტესტავთ თქვენს უნარებს)  შექმენით პროგრამა სადაც მომხმარებელს input ფუნქციის საშუალებით შემოატანინებთ თავის ასაკს, შემდეგ ეს ასაკი გარდაქმენით მთელ რიცხვად (რადგან შემოტანილი რიცხვი სტრინგის ფორმატში იქნება თავიდან), საბოლოოდ კი if else_ის საშუალებით დაბეჭდეთ შესაბამისი ტექსტები, თუ მომხმარებლის ასაკი >= 18 დაბეჭდეთ რომ ის არის ზრდასრული, სხვაშემთხვევაში დაუბეჭდეთ რომ ის არის არასრულწლოვანი

#რესურსები რომელსაც გამოიყენებთ იმ თემების შესასწავლად რაც ჯერ არ იცით: input, int, if else - ამათი სწავლა მოგიწევთ დამოუკიდებლად.
#1) input function - https://www.w3schools.com/python/ref_func_input.asp
#2) int function  - https://www.w3schools.com/python/ref_func_int.asp
#3) if else - არ გეტყვით :დდ დასერჩეთ ბრაუზერში და თქვენით მოიძიეთ, არ დაგავიწყდეთ პითონს სწავლობთ
#W3Schools offers free online tutorials, references and exercises in all the major languages of the web. Covering popular subjects like HTML, CSS, JavaScript, Python, SQL, Java, and many, many more.
#Image
#W3Schools offers free online tutorials, references and exercises in all the major languages of the web. Covering popular subjects like HTML, CSS, JavaScript, Python, SQL, Java, and many, many more.


age = int(input("enter your age: "))


if age >= 18:
     print("you are an adult")
else:
     print("you are underage")