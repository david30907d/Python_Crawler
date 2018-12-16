$('li.service_name a').each((index, value) => {
	// let s = "https://case.518.com.tw/workroom-service_detail-2355459.html?sid=32599";
	let s = $(value).attr("href")
	let result = s.match(/\d+/g).map(n => parseInt(n));
	console.log(result[0], result[1])
	$.ajax({
	  method: "POST",
	  url: "https://case.518.com.tw/ajax/",
	  data: {"module": "workroom",
		"action": "set_service_msg",
		"service_request_type": 2,
		"service_type": 1,
		"ssid": result[1],
		"mid": result[0],
		"msg_type": "服務內容詢問",
		"msg_content": "您好，拍攝時裝 \n拍攝地點為台北新北市 \n假日都行，平日的話需要討論 \n 請問您方便的日期和價碼（須加車馬費嗎？）\n 我的line: davidtnfsh email: davidtnfsh@gmail.com \n 因為我是大批量詢問518上的model，所以當您回信時麻煩註明您是哪一位518的平面模特兒（順便附上您的518網址，幫助我回憶您是哪位），如有不便請多包涵",
		"msg_name": "張泰瑋",
		"msg_tel": "0972804840",
		"msg_email": "davidtnfsh@gmail.com"}
	})
})