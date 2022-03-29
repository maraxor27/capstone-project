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
		fileInput(){
			this.clear()
			
		},
		doWhile(){
			this.clear() // clear inputs first
			this.assemblyCode = 
			`BIN_TEST EQU %00010101
OCTAL_TEST EQU @40
HEXA_TEST EQU $42
INT_TEST EQU 56
			
global_char_arr DS.B 20
global_const_char_arr DC.B 'this is a test'
			
; Stack
OFFSET 0
F_X DS.W 1  	; save X
F_Y DS.W 1  	; save Y
F_RA DS.W 1 	; return address
F_SRC DS.W 1    ; short int *src
F_DST DS.W 1    ; short int *dst
F_SIZE DS.B 1   ; char size
			
memcopy:
	pshy
	pshx
	ldx F_SRC, SP
	ldy F_DST, SP
	ldab #0
loop:
	movw 0,x , 0,y
	inx
	iny
	incb
	cmpb F_SIZE, SP
	blo loop
endloop:
	pulx
	puly
	rts`
		},
		forLoop(){
			this.clear() // clear inputs first
			this.assemblyCode = 
			`N equ 20 ; array count

OFFSET 0
p_ra ds.w 1 ; return address
sum ds.w 1 ; array sum
i ds.b 1 ; array index

program:
	ldaa #0
	staa i
	staa sum
	staa sum+1
	ldaa sum+1
loop: 
	ldab i
	cmpb #N
	beq done
	ldx #array
	leax b,x; abx
	ldab 0,x
	ldy sum
	leay b,y; aby
	sty sum
	inc i
	bra loop
done: 
	swi 	

array dc.b 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20`
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
			<!--
				1. Enter some assembly code you wish to convert to C in the left text area<br>
				2. Press the « Decompile For Me » button<br>
				3. You will see the converted code displayed in the right text area<br>
			-->
			</div>


      		<div class="container">
				<div class="row text-center" style="text-align: center;">
					<div class="col-md-4">
						<span class="fa-stack fa-4x">
							<i class="fas fa-circle fa-stack-2x text-primary"></i>
							<i class="fas fa-shopping-cart fa-stack-1x fa-inverse"></i>
						</span>
						<h4 class="service-heading">1.</h4>
						<p class="text-muted">
						Enter some assembly code you wish to convert to C in the left text area
						</p>
					</div>
					<div class="col-md-4">
						<span class="fa-stack fa-4x">
							<i class="fas fa-circle fa-stack-2x text-primary"></i>
							<i class="fas fa-laptop fa-stack-1x fa-inverse"></i>
						</span>
						<h4 class="service-heading">2.</h4>
						<p class="text-muted">
						Press the « Decompile For Me » button
						</p>
					</div>
					<div class="col-md-4">
						<span class="fa-stack fa-4x">
							<i class="fas fa-circle fa-stack-2x text-primary"></i>
							<i class="fas fa-lock fa-stack-1x fa-inverse"></i>
						</span>
						<h4 class="service-heading">3.</h4>
						<p class="text-muted">
						You will see the converted code displayed in the right text area
						</p>
					</div>
				</div>
			</div>


		</div>
		
		<table style="margin: auto; width: 90%">
			<tr>
				<th class="codeTableHeader" style="width: 49%">
					<div class="expandingArea">
						<pre><span></span><br></pre>
						<textarea id="content-target" placeholder="Enter Assembly Here" v-model="assemblyCode" style="resize: none !important" class="fileContent">
						</textarea>
					</div>
				</th>
				<th class="codeTableHeader" style="width: 49%; height: 505px; vertical-align: top;">	
					<prism-editor class="my-editor" v-model="cCode" :highlight="highlighter" line-numbers></prism-editor>
				</th>
			</tr>
		</table>

		<div style = "text-align: right; margin: 30px auto; width: 210px;">
			<div>
				<input type="file" id="input-file" style="text-align: center; margin-bottom: 5px;" onchange="fileInput()" accept=".asm, .inc"/>
			</div>
			
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

			<div style="text-align: center;">
					<b-button variant="primary" @click="doWhile()">Do While</b-button>
					<b-button variant="primary" @click="forLoop()">For Loop</b-button>		
			</div>
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
