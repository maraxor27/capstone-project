Vue.component('myheader', {
	data: function() {
		return {
			email: "",
			password: "",
			user: {},
			logged_in: false,
			error_message: "",
		}
	},
	created: function() {
		axios({
			method: 'post',
			url: '/login',
		}).then((response) => {
			this.login_success(response)
		}, (error) => {})
	},
	methods: {
		login(email, password) {
			axios({
				method: 'post',
				url: '/login',
				data: {
					'email': email,
					'password': password
				}
			}).then((response) => {
				this.login_success(response)
			}, (error) => {
				console.log(error)
				this.error_message = "Invalid email password combination"
			})
		},
		login_success(response) {
				this.user = response.data
				this.error_message = ""
				this.logged_in = true
				this.email = ""
				this.password = ""
				this.$emit('user-update', this.user)
		},
		logout() {
			axios({
				methods: "post",
				url: "/logout",
			}).then((response) => {
				this.user = {}
				this.logged_in = false
				this.$emit('user-update', this.user)
			})
		},
	},
	template:
	`
	<div>
		<b-navbar type="dark" variant="dark">
			<b-navbar-nav>
				<b-nav-item href="">Home</b-nav-item>
			</b-navbar-nav>
			<b-navbar-nav class="ml">
				<b-nav-item-dropdown text="User" v-if="!logged_in" right>
					<li class="no-wrap" style="min-width: 17rem; margin: 4px;">
						<div class="input-group input-group-sm mb-3">
							<div class="input-group-prepend" style="width:6rem;">
								<span class="input-group-text" id="inputGroup-sizing-sm">Email</span>
							</div>
							<input type="text" class="form-control" 
								v-model="email"
								aria-label="Small" aria-describedby="inputGroup-sizing-sm">
						</div>
					</li>
					<li class="no-wrap" style="min-width: 17rem; margin: 4px;">
						<div class="input-group input-group-sm mb-3">
							<div class="input-group-prepend" style="width:6rem;">
								<span class="input-group-text" id="inputGroup-sizing-sm">Password</span>
							</div>
							<input type="text" class="form-control" 
								v-model="password"
								aria-label="Small" aria-describedby="inputGroup-sizing-sm">
						</div>
					</li>
					<li v-show="error_message != ''" style="color: red; margin-bottom: 1rem;">{{ error_message }}</li>
					<li style="margin: 4px;">
						<button class="btn btn-dark" style="margin: auto;" 
							v-on:click="login(email, password)">
							connect
						</button>
					</li>
				</b-nav-item-dropdown>
				<b-nav-item-dropdown 
						v-bind:text="user.email" 
						v-else right>
					<b-dropdown-item href="">Account</b-dropdown-item>
					<b-dropdown-item href="">Settings</b-dropdown-item>
					<li style="margin: 4px;">
						<button class="btn btn-dark" style="margin: auto;" 
							v-on:click="logout()">
							logout
						</button>
					</li>
				</b-nav-item-dropdown>
			</b-navbar-nav>
		</b-navbar>
	</div>
	`
})