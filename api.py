from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

STUDENTS = {
  '1': {'Status': 'True', 'UserId': 'abc', 'emailId': 'abc@gmail.com', 'collegeRollNum' : 1786, 'arrNum' : '[1,2,3]', 'arrAlph' : '[a,b,c]'},
  '2': {'Status': 'False', 'UserId': 'xyz', 'emailId': 'xyz@gmail.com', 'collegeRollNum' : 1819, 'arrNum' : '[1,22,32]', 'arrAlph' : '[a,s,p]'},
  '3': {'Status': 'True', 'UserId': 'john', 'emailId': 'john@gmail.com', 'collegeRollNum' : 19191, 'arrNum' : '[12,2,3]', 'arrAlph' : '[a,b,c]'},
  '4': {'Status': 'True', 'UserId': 'sid', 'emailId': 'sid@gmail.com', 'collegeRollNum' : 2922, 'arrNum' : '[1,2,322]', 'arrAlph' : '[a,c,s]'}
}

parser = reqparse.RequestParser()
class StudentsList(Resource):
  def get(self):
      return STUDENTS
  def post(self):
      parser.add_argument("Status")
      parser.add_argument("UserId")
      parser.add_argument("emailId")
      parser.add_argument("collegeRollNum")
      parser.add_argument("arrNum")
      parser.add_argument("arrAlph")
      args = parser.parse_args()
      student_id = int(max(STUDENTS.keys())) + 1
      student_id = '%i' % student_id
      STUDENTS[student_id] = {
        "Status": args["Status"],
        "UserId": args["UserId"],
        "emailId": args["emailId"],
        "collegeRollNum": args["collegeRollNum"],
        "arrNum": args["arrNum"],
        "arrAlph": args["arrAlph"]
      }
      return STUDENTS[student_id], 201



api.add_resource(StudentsList, '/students/')



if __name__ == "__main__":
  app.run(debug=True)







