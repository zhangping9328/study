#[]代表list,{}代表dict
person = {
    'name':'zhangping',
    'age':28,
    'sex':'女'

}
xiaoming = {
    'name':'zhangping1',
    'age':27,
    'id':1
}
person.update(xiaoming)
print(person)