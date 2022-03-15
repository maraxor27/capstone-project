Vue.component('home', {
	data: function() {
		return {
			assembCode: "",
			cCode:"",
		}
	}, 

	method:{
		makeExpandingArea(container) {
			var area = container.querySelector('textarea');
			var span = container.querySelector('span');
			if (area.addEventListener) {
				area.addEventListener('input', function() {
					span.textContent = area.value;
				}, false);
				span.textContent = area.value;
			} else if (area.attachEvent) {

			// IE8 compatibility
			area.attachEvent('onpropertychange', function() {
				span.innerText = area.value;
			});
			span.innerText = area.value;
		}
		// Enable extra CSS
		container.className += "active";
	},
},
				
//Display of the home page
	template:
	`
	<div> 
		<div class="bg-light" style = "padding: 20px 0px 20px 0px ">
			<div style = "text-align:left; margin: auto; width: 50%;">
				<h4 style = "text-align:center; padding-top: 20px">How to use this tool:</h4><br>

				1. Enter some assembly code you wish to convert to C in the left text area<br>
				2. Press the « Decompile For Me » button<br>
				3. You will see the converted code displayed in the right text area<br>
			</div>
		</div>
		<ul class="sideBySide" >
			<li>
				<!-- Input Text box for assembly -->
				<div class="expandingArea">
					<pre><span></span><br></pre>
					<textarea placeholder="Enter Assembly Here" v-model = "assembCode">
					</textarea>
				</div>
			</li>

			<li>
				<div class="expandingArea">
					<pre><span></span><br></pre>
					<textarea placeholder="Your decompiled code will show up here" v-model="cCode "></textarea>
				</div>
			</li>
		</ul>

		<div style = "text-align: right; margin-right: 90px; margin-bottom: 20px;">
			<b-button variant="primary">Decompile For Me</b-button>
		</div>

		<div class="bg-light" style = "padding: 20px 0px 20px 0px ">
			<div style = "text-align:left; margin: auto; width: 50%;">
				<h4 style = "text-align:center; padding-top: 20px">Examples:</h4>
				<h6 style = "text-align:center;" class="text-muted">Press the buttons corresponding to the example then press the Decompile For Me button <br></h6>
			</div>

			<ul class="sideBySide" >
				<li>
					<b-button variant="primary">Do While</b-button>
				</li>
				<li>
					<b-button variant="primary">Print</b-button>
				</li>

				<li>
					<b-button variant="primary">If Statement</b-button>
				</li>
				<li>
					<b-button variant="primary">For Loop</b-button>
				</li>
				
			</ul>
		</div>

	</div>
			`
})
