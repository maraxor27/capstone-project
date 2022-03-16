Vue.component('home', {
	data: function() {
		return {
			assemblyCode: "",
			cCode:"",
		}
	}, 

	methods: {
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
		decompile() {
			axios({
				method: 'POST',
				url: '/api/v2/decompiler',
				data: {
					'assembly': this.assemblyCode,
					'arch':"68HC12",
					/* arch is there if the application 
					supports many arch in the future*/
				}
			}).then((response) => {
				this.cCode = response.data.cCode
			},(error) => {
				console.log(error)
			})
		}, 
		clear(){
			this.cCode = ""
			this.assemblyCode = ""

		},
		highlighter(cCode) {
      // js highlight example
      return Prism.highlight(cCode, Prism.languages.clike, "c");
    }

	},
				
	//Display of the home page
	template:
	`
	<div style="background-color: #f8f9fa"> 
		<div class="bg-light" style = "padding: 20px 0px 20px 0px ">
			<div style = "text-align:left; margin: auto; width: 50%;">
				<h4 style = "text-align:center; padding-top: 20px">How to use this tool:</h4><br>

				1. Enter some assembly code you wish to convert to C in the left text area<br>
				2. Press the « Decompile For Me » button<br>
				3. You will see the converted code displayed in the right text area<br>
			</div>
		</div>
		
		<table style="margin: auto; width: 90%">
			<tr>
				<th class="codeTableHeader" style="width: 49%">
					<div class="expandingArea">
						<pre><span></span><br></pre>
						<textarea placeholder="Enter Assembly Here" v-model="assemblyCode" style="resize: none !important">
						</textarea>
					</div>
				</th>
				<th class="codeTableHeader" style="width: 49%; height: 505px; vertical-align: top;">	
					<prism-editor class="my-editor" v-model="cCode" :highlight="highlighter" line-numbers></prism-editor>
				</th>
			</tr>
		</table>

		<div style = "text-align: right; margin: 30px auto; width: 210px;">
			<b-button variant="primary" @click="decompile()">Decompile For Me</b-button>
			<b-button variant="danger" @click="clear()">
				<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
  				<path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
 				 <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
				</svg>
			</b-button>
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




		

		// <ul class="sideBySide" >
		// 	<li>
		// 		<!-- Input Text box for assembly -->
		// 		<div class="expandingArea">
		// 			<pre><span></span><br></pre>
		// 			<textarea placeholder="Enter Assembly Here" v-model="assemblyCode">
		// 			</textarea>
		// 		</div>
		// 	</li>

		// 	<li>
		// 		<prism-editor class="my-editor height-200" v-model="cCode" :highlight="highlighter" line-numbers></prism-editor>
		// 	</li>
		// </ul>