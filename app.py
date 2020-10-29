from flask import Flask
import subprocess
app = Flask(__name__)

#mostra a aplicação no "/"
@app.route("/")
def hello():
    return "<h1 style='color:green'> ae!!!</h1>"

#retorna user: user
#Uso:
# http://ip:80/user/lucas
@app.route('/user/<username>')
def show_user_profile(username):
    return "<marquee> User: %s</marquee>" % username

#retorna post, somente aceitando numeros "int:"
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

#retorna o hostname onde ele foi executado,
#util para testar o funcionamento do cluster
@app.route("/host")
def host():
    cmd = [ "hostname"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                              stderr = subprocess.PIPE,
                              stdin = subprocess.PIPE)
    out,err = p.communicate()
    return out

if __name__ == "__main__":
    app.run()