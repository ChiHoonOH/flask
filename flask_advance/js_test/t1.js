console.log('hello js');
var name = '부산';  //변수
const NAME2= '부산2';   //상수->값을 변경 할 수 없다.
let name3='부산'//지역은 지역대로 전역은 전역대로
//name2='111';//상수는 변경 불가.
//함수 
console.log(add(1,2));//함수가 먼저 올라 오기 때문에 위에 쓸 수 있다.
function add(x,y)
{return x+y;}

console.log(add(1,2));

//자바스크립트의 변수는 모든 것을 받을 수 있다.

//익명함수(함수 이름이 없는거,콜백함수 사용시=>클로저)
//용도: 1회성으로 사용시
// console.log(add2(3,5));  //메모리에 올라가는건 변수에 저장될때임
//그래서 정의한 이후에 사용한다.
var add2 = function(x,y){
    return x+y;
}

console.log(add2(3,5));

//콜백함수 : 함수의 인자로 함수를 넣는다.
//왜 : 비동기상황(i/o)에서 결과를 언제 받을지 모를때(파이썬에 잇는 공간 말고 다른공간에 왓다갓다 할때?)

function test(x,y,cb){
    cb(x,y);
}

// test(1,2,function(x,y){
//     console.log(`${a}+${b}=${a+b}`);
// });
//모던 자바스크립트 에로우 함수 => 표현은 간단하게
//function 제거
//인자값이 1개면 () 제거
//(){} 사이에=>추가
//수행문이 하나면 {}제거(retrun이 존재할때)
//return이 존재하지 않으면 {}를 그대로 써줘야한다.

// test(1,2,(x,y)=>{console.log(`${a}+${b}=${a+b}`)});


//객체 및 클래스 정의
//4가지 존재 => 표준안 추가(babel로 변환해서 처리,브라우져에서 지원해주고 있지 않아서 쓰지 않는다.)
//1.객체, 리터럴
//1회성 객체,인자가 많아서 한번에 통으로 인자로 전달시 사용
var obj = {
    name:'부산',
    getName:()=>{
        return this.name;
    }
}

function ok(x,y){
    return x+y;
}

console.log(obj)
console.log(obj.name)
console.log(obj.getName)

//무명함수
function k(){}
function a(){
    return 'good'
}
k1:()=>{
    return 'hh'
} 

var person={
    name : 'ningen',
    bsabjil:()=>{return 'siba'},
    basi:(a,b)=>{return a+b},
    basi2: a=>{return a},
    basi3: (a,b)=>a+b,//파이썬 람다 함수와 거의 동일한 형태
    basi4: (a,b)=>a+b
}

function run(a){a=a+1}//이거 됨
run2:a=>{a=a+1} //function 삭제






