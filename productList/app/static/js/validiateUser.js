var flag1 =0;
var flag2 =0;
var flag3 =0;
function validateUn() {
  var x = document.getElementById("validationDefault05");

  var username  = x.value;

  ajaxFunction(username,"username");
}

function validateEmail() {
  var x = document.getElementById("validationDefault03");

  var email  = x.value;

  ajaxFunction(email,"email");
}


function ajaxFunction(username,type)
{
  $.ajax(
{
    type:"GET",
    url: "/validiateUser/",
    data:{
             data: username,
             type:type

    },
    success: function( data )
    {
        if(type=="email"){
            document.getElementById("emailHelp").innerHTML=data.result;
            if(data.result=="OK"){
                flag1 = 1;
                enableDisableBtn();
            }
        }
        else{
          document.getElementById("userNameHelp").innerHTML=data.result;
          if(data.result=="OK"){
              flag2 = 1;
              enableDisableBtn();
          }
        }


    }
 });

}

function comparePassword(){
  pass = document.getElementById("validationDefault06").value;
  cPass = document.getElementById("validationDefault07").value;
  if (pass != cPass){
    document.getElementById("cPasswordHelp").innerHTML="Confirm password does't match with password";
  }
  else{
    document.getElementById("cPasswordHelp").innerHTML="OK";
    flag3 = 1;
    enableDisableBtn();
  }
}

function enableDisableBtn(){
  if (flag1==0 || flag2==0 || flag3==0){
    document.getElementById("submit").disabled = true;
  }
  else{
    document.getElementById("submit").disabled = false;
  }
}
