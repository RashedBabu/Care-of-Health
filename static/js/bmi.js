document.getElementById('bmi-form').addEventListener('submit', calculateResults)

function calculateResults(e){
	var weight = document.getElementById('weight').value
	var h_in_ft  = document.getElementById('ft').value
	var h_in_inch  = document.getElementById('inch').value
	var height = (parseFloat(h_in_ft *12) + parseFloat(h_in_inch))* 0.0254

	var result = document.getElementById('res')

	var calculated_bmi = parseFloat(weight) / (height*height)

	result.value = calculated_bmi.toFixed(2)

	e.preventDefault()
}