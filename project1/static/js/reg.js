
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#sub').disabled = true;
    document.querySelector('#use').onkeyup = () => {
        document.getElementById("error").innerHTML = "This credentail is not allowed"
        if (document.querySelector('#use').value.length > 0 && document.querySelector('#use').value.includes('@') == true) {
            document.getElementById("error").innerHTML = ""
            document.querySelector('#pass').onkeyup = () => {
                if (document.querySelector('#pass').value.match(/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$@$!%* #+=\(\)\^?&])[A-Za-z\d$@$!%* #+=\(\)\^?&]{6,}$/)) {
                    document.querySelector('#sub').disabled = false;
                    document.getElementById("error").innerHTML = ""
                }
                else {
                    document.querySelector('#sub').disabled = true;
                    document.getElementById("error").innerHTML = "This credentail is not allowed"
                }
            }

        }
        else {
            document.querySelector('#sub').disabled = true;
            document.getElementById("error").innerHTML = "This credentail is not allowed"
        }
    };
    return false;
});