console.log("1");

//문서(HTML document)가 브라우저 메모리에 모두 로드 되었다.
//이 이벤트가 발생하면 호출된다.
//$('css selector') <-jquery의 요소를 표현한 방법
//DOM(Document Object Model)
//문서가 준비되면 콜백함수를 하나 넣어줄테니 호출해라.
// $(document).ready(()=>{
//     console.log("3");
// })
$(document).ready(function(){
    //문서가 화면에 보기에 직전에 할일 구현

    //form 태그에서 submit 이벤트가 발생하면
    //이벤트를 인터셉트해서 무효화 하고 
    //ajax 통신을 수행한다.
    //$(셀렉터).on('이벤트명','콜백함수) ??콜백함수
    //특정 요소의 이벤트를 내맘대로 재정의
    $('form').on('submit',(evt)=>{
        evt.preventDefault();//기존의 이벤트 중단.
        console.log('검색 클릭')
        //ajax 구성 : 통신, 현재화면유지하면서 통신후 파싱 ->
        //          화면을 동적으로 변경(Dom 조작)
        $.post({
            url:'/search',     //접속주소
            data:$('form').serialize(),    //전달 데이터: 키=값 & 키=값 한번에 다해주기
            //data:'keyword=삼성전자',
            
            dataType:'json', //응답 데이터
            success:(data)=>{
                //서버로부터 응답이 오면 여기서 부터 코드가 진행됨.
                console.log('성공:',data);
                //결과 처리는 =>js(jquery) 해결
                $('#result').empty();
                //검색어 획득
                const keyword = $('input[name=keyword]').val()//var 속성값
                // var html='';
                $.each(data,(idx,item)=>{
                    // 데이터를 하나씩 획득
                    console.log(idx,item);//item is dictionary
                    var html = `
                    <div>
                        <span>종목이름:${item.name.replace(keyword,`<b>${keyword}</b>`)}</span>
                        <span>종목코드:${item.code}</span>
                        <span>현재가:${item.cur}</span>
                    </div>                    
                    `;// python '''랑 같은 효과
                    //item.name.replace()를 해줄 수도 있으나 반복 돌아버림 
                    $('#result').append(html);
                    //이벤트 -> 1찾기 2. 적용
                    //여기서는 first가 last second가 last항상 마지막 추가된것이 last이므로
                    $('#result>div:last').on('click',()=>{
                        //???????????????
                        //usl_for() 통해서 url를 표시하는 것이 맞으나
                        //home.js가 랜더링의 대상이 되는 html외부에 있어서
                        //해당 함수는 반영이 되지 않는다.

                        document.location.href=`/info?code=${item.code}`;
                        //``(숫자 1앞에 있는거다.)
                    });       //방금 추가된놈
                   //on('이벤트명',콜백함수)
                });
                //$('#result').append(html.replace(keyword,'<b>${keyword}</b>'));//이거 지역 변수 아닌가?
                //검색어 자리에 글자 표현
                $('#keywordShow').empty().append(keyword);
                $('input[name=keyword]')
                //검색창에 검색어 제거
               
            }, //통신성공
            error:(err)=>{
                console.log('실패:',err)
            } //통신실패
        }); //순수 jquery 함수, {} =>객체
        return false;//이벤트 실패(위의 preventDefault 함수가 특정값을 반환할 것이므로.)
    });//on => 자바스크립트의 event

});

function call()
{
    alert('hello');//너님도 순수 함수
    //ctrl+shift+R=>강력한 새로고침
}

//alert('call');