function ShowCommentForm(id){
    $("#" + id).removeClass('hidden');
}
function HideCommentForm(id){
    $("#" + id).addClass('hidden');
}

function validateForm() {
    var x = document.forms["comment-form"]["subject"].value;
    var y = document.forms["comment-form"]["comment"].value;
    if (x == null || x == "") {
        alert("Please enter subject");
        return false;
    }
    if (y == null || y == "") {
        alert("Please enter comments");
        return false;
    }
}
function editvalidateForm(){
    var x = document.forms["edit-comment-form"]["subject"].value;
    var y = document.forms["edit-comment-form"]["comment"].value;
    if (x == null || x == "") {
        alert("Please enter subject");
        return false;
    }
    if (y == null || y == "") {
        alert("Please enter comments");
        return false;
    }
	
}