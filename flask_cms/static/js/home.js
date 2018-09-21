// 콘솔 출력
console.log("1");

// 문서(HTML document)가 브라우저 메모리에 모두 로드 되었다 => 준비되었다 
// 이 이벤트가 발생하면 호출된다
// $('css selector') <- jquery의 요소를 표현한 방법
// DOM( Document Object Model)
// 문서가 준비되면 콜백함수를 하나 넣어줄테니 호출해라
$(document).ready( function () {
  // 문서가 화면에 보이기 직전에 할일 구현

  // form 태그에서 submit 이벤트가 발생하면
  // 이벤트를 인터셉트해서 무효화 하고
  // ajax 통신을 수행하여 화면처리한다
  // $(셀렉터).on('이벤트명', 콜백함수)
  // 튻정 요소의 이벤트를 내맘대로 재정의
  $('form').on('submit', (evt)=>{
    // submit(form 데이터 전송이벤트) 이벤트 중단
    evt.preventDefault();
    console.log('검색 클릭');
    // ajax 구성 : 통신 (검색), 현재화면유지하면서 통신후 파싱->
    //             화면을 동적으로 변경 (DOM 조작)
    $.post({
      url:'/search',      // 접속 주소
      data:$('form').serialize(), // 전달 데이터 => 키=값&키=값      
      //data:'keyword=삼성전자',
      dataType:'json', // 응답 데이터 포멧
      success:(data)=>{
        // 서버로 부터 응답이 오면 여기서부터 코드가 진행됨
        console.log('성공:', data);  
        // 결과 처리는 => js (jquery) 해결
        // 기존 결과를 비운다
        $('#result').empty();
        // 검색어 획득
        const keyword = $('input[name=keyword]').val();
        //var html      = '';
        $.each( data, (idx, item)=>{
          // 데이터를 하나씩 획득
          console.log(idx, item);          
          var html = `
            <div>
              <span>종목이름:${item.name.replace(keyword, `<b>${keyword}</b>`)}</span>
              <span>종목코드:${item.code}</span>
              <span>현재가:${item.cur}</span>
            </div>
          `;
          $('#result').append( html );
          // 이벤트 적용:찾아서 적용해라
          // 의사 결정 셀렉터 #result 요소의 직계자식 div들중에 막내
          $('#result>div:last').on('click', ()=>{
            // url_for() 통해서 url를 표시하는것이 맞으나
            // home.js가 랜더링의 대상이 되는 html 외부에 있어서
            // 해당 함수는 반영이 않된다
            document.location.href=`/info?code=${item.code}`;
          });
        } );
        
        // 검색어 자리에 글자 표현
        $('#keywordShow').empty().append(keyword);
        // 검색창에 검색어 제거 
        $('input[name=keyword]').val(''); 
      }, // 통신성공
      error:(err)=>{
        console.log('실패:', err);
      },   // 통신실패
    });


    // 이벤트 실패
    return false;
  } );

} );

function call()
{
  alert('hello');
}