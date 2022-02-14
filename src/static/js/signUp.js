Vue.component('signup', {
	props: ['user'],
	data: function() {
		return {
			form: {
				firstname: "",
				lastname:"",
				email: "",
				password: "",
			},
			passwordConfirmation: "",
			showErrorMessage: false,
			showSuccessMessage: false,
			errorMessage: "",
		}
	},
	methods: {
		signUp(event) {
			axios({
				method: 'post',
				url:'/api/v2/users/',
				data: {
					firstname: this.form.firstname,
					lastname: this.form.lastname,
					email: this.form.email,
					password: this.form.password,
				},
			}).then((response) => {
				this.showSuccessMessage = true
				this.showErrorMessage = false
			}, (error) => {
				console.log(error.message)
				this.showSuccessMessage = false
				this.showErrorMessage = true
				this.errorMessage = error.response.data.message
			})
		},
		resetForm(event) {},
	},
	computed: {
		firstnameValidation() {
			if (this.form.firstname.length == 0)
				return null
			return /^([a-z]|[A-Z]|[- ]){1,100}$/gm.test(this.form.firstname)
		},
		lastnameValidation() {
			if (this.form.lastname.length == 0)
				return null
			return /^([a-z]|[A-Z]|[-]){1,100}$/gm.test(this.form.lastname)
		},
		emailValidation() {
			if (this.form.email.length == 0)
				return null
			if (this.form.email.length > 100)
				return false
			// This regex is from https://emailregex.com
			re = /^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$/gm
			return re.test(this.form.email)
		},

		//Verify if passwords matches and if they respect conditions
		//Conditions:
		//1.Can't be nothing 2.Can't be <10 characters 3. Can't be > 255 characters
		passwordValidation() {
			if (this.form.password.length == 0)
				return null
			if (this.form.password.length < 10)
				return false
			if (this.form.password.length > 255)
				return false
			if (/[ ]/gm.test(this.form.password))
				return false
			return /[A-Z]/gm.test(this.form.password) && /[a-z]/gm.test(this.form.password) && /\d/gm.test(this.form.password)
		},
		passwordConfirmationValidation() {
			if (this.passwordConfirmation.length == 0)
				return null
			return this.form.password == this.passwordConfirmation
		},
	},
				
//Display of the sign up page
	template:
	`<div class="container">
		<b-form>
			<h1>Register</h1>
			<p>Please fill in this form to create an account.</p>

			<hr>
			<label for="firstname"><b>First Name</b></label>
			<b-form-group id="input-group-1" label-for="input-1">
				<b-form-input
					id="input-1"
					v-model="form.firstname"
					placeholder="Enter first name"
					size="lg"
					required
				></b-form-input>
				<b-form-invalid-feedback :state="firstnameValidation">
					Your first name must be 1-100 letters long
				</b-form-invalid-feedback>
				<b-form-valid-feedback :state="firstnameValidation">
					All good!
				</b-form-valid-feedback>
			</b-form-group>

			<label for="lastname"><b>Last Name</b></label>
			<b-form-group id="input-group-2"  label-for="input-2">
				<b-form-input
					id="input-2"
					v-model="form.lastname"
					placeholder="Enter last name"
					size="lg"
					required
				></b-form-input>
				<b-form-invalid-feedback :state="lastnameValidation">
					Your last name must be 1-100 letters long
				</b-form-invalid-feedback>
				<b-form-valid-feedback :state="lastnameValidation">
					All good!
				</b-form-valid-feedback>
			</b-form-group>

			<label for="email"><b>Email</b></label>
			<b-form-group id="input-group-3" label-for="input-3">
				<b-form-input
					id="input-3"
					v-model="form.email"
					placeholder="Enter Email"
					size="lg"
					required
				></b-form-input>
				<b-form-invalid-feedback :state="emailValidation">
					Invalid email
				</b-form-invalid-feedback>
				<b-form-valid-feedback :state="emailValidation">
					All good!
				</b-form-valid-feedback>
			</b-form-group>

    		<label for="psw"><b>Password</b></label>
    		<b-form-group id="input-group-4" label-for="input-4">
				<b-form-input
					id="input-4"
					v-model="form.password"
					placeholder="Enter Password"
					type="password"
					size="lg"
					required
				></b-form-input>
				<b-form-invalid-feedback :state="passwordValidation">
					Password must be 10 to 255 character long and must contain the following: uppercase, lowercase, numbers.
					No space allowed!
				</b-form-invalid-feedback>
				<b-form-valid-feedback :state="passwordValidation">
					All good!
				</b-form-valid-feedback>
			</b-form-group>

    		<label for="psw-repeat"><b>Repeat Password</b></label>
    		<b-form-group id="input-group-5" label-for="input-5">
				<b-form-input
					id="input-5"
					v-model="passwordConfirmation"
					placeholder="Repeat Password"
					type="password"
					size="lg"
					required
				></b-form-input>
				<b-form-invalid-feedback :state="passwordConfirmationValidation">
					Passeword does not match
				</b-form-invalid-feedback>
				<b-form-valid-feedback :state="passwordConfirmationValidation">
					All good!
				</b-form-valid-feedback>
			</b-form-group>
			<hr>
			<p>By creating an account you agree to our <a href="#">Terms of Use</a>.</p>
			<b-button variant="primary" @click="signUp">Submit</b-button>
			<b-button type="reset" variant="danger">Reset</b-button>
		</b-form>
		<div>
			<div style="color: green; margin: auto;" v-if="showSuccessMessage">
				New account created successfuly 
			</div>
			<div style="color: red; margin: auto;" v-if="showErrorMessage">
				Error while trying to create a new account 
				<br>
				{{ errorMessage }}
			</div>
 		 </div>
	</div>
	`
})