const img = document.getElementById("selectedImage");
const canvas = document.getElementById("imgCanvas");

const changeImage = (input) => {
  console.log(img);
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      img.src;
      img.setAttribute("src", e.target.result);
    };

    reader.readAsDataURL(input.files[0]);
  }
};
