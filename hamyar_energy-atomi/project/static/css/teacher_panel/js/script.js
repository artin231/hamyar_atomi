let header = document.querySelector('.header');
let r = document.querySelector(':root');
let gg = document.getElementById('gg');
let li = document.querySelector('.d1');
let li2 = document.querySelector('.d2');
let btn_color = document.querySelector('.btn-color');
let pr = document.querySelector('.profile');
let ul = document.querySelector('ul');
let nav = document.querySelector('nav');



header.style.transition = 'all 200ms ease';


let isuenuOpen = false;
gg.addEventListener('click', (e) => {
    if (!isuenuOpen) {
        pr.classList.add('pr');
        header.classList.add('bighead');
        li.classList.add('block');
        li2.classList.add('block');
        btn_color.classList.add('block');
        ul.classList.add('ul');
        nav.classList.add('nav');
        isuenuOpen = true;
    }
    else {
        header.classList.remove('bighead');
        pr.classList.remove('pr');
        li.classList.remove('block');
        li2.classList.remove('block');
        btn_color.classList.remove('block');
        ul.classList.remove('ul');
        nav.classList.remove('nav');
        isuenuOpen = false;
    }

});

let click = false;
btn_color.addEventListener('click', (e) => {
    if (!click) {
        btn_color.innerHTML = 'تم شب';
        btn_color.classList.add('white');

        click = true;
        r.style.setProperty('--color1', '#BDBDBD');
        r.style.setProperty('--color2', '#e0e0e0');
        r.style.setProperty('--color3', '#FAFAFA');
        r.style.setProperty('--color_w', 'black');



    }
    else {
        btn_color.innerHTML = 'تم روز';
        r.style.setProperty('--color1', '#2b2b2b');
        r.style.setProperty('--color2', '#5a5a5a');
        r.style.setProperty('--color3', '#949494');
        r.style.setProperty('--color_w', 'white');
        btn_color.classList.remove('white');
        click = false;
    }
});
