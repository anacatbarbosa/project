// div where content will be added
const profileDiv = document.querySelector('#myProfile');
const nameButton = document.getElementById('nameChange');
const emailButton = document.getElementById('emailChange');
const pwButton = document.getElementById('pwChange');
const adminButton = document.getElementById('addAdmin');

function changeName() {
    profileDiv.innerHTML = `
        <div class="changeName">
            <form method="post" action="/profile/name">
                <div class="form-group row">
                    <label for="oldName" class="col-sm-2 col-form-label">Old Username</label>
                    <div class="col-sm-10">
                        <input type="text" class="form-control" name="oldName" id="oldName" placeholder="Old Username">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="newName" class="col-sm-2 col-form-label">New Username</label>
                    <div class="col-sm-10">
                        <input type="text" class="form-control" name="newName" id="newName" placeholder="New Username">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-sm-10">
                        <button type="submit" class="btn btn-primary">Change Username</button>
                    </div>
                </div>
            </form>
        </div>
    `
}

function changeEmail() {
    profileDiv.innerHTML = `
        <div class="changeEmail">
            <form method="post" action="/profile/email">
                <div class="form-group row">
                    <label for="oldEmail" class="col-sm-2 col-form-label">Old E-mail</label>
                    <div class="col-sm-10">
                        <input type="email" class="form-control" name="oldEmail" id="oldEmail" placeholder="Old E-mail">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="newEmail" class="col-sm-2 col-form-label">New E-mail</label>
                    <div class="col-sm-10">
                        <input type="email" class="form-control" name="newEmail" id="newEmail" placeholder="New E-mail">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-sm-10">
                        <button type="submit" class="btn btn-primary">Change E-mail</button>
                    </div>
                </div>
            </form>
        </div>
    `
}

function pwChange() {
    profileDiv.innerHTML = `
        <div class="changePw">
            <form method="post" action="/profile/password">
                <div class="form-group row">
                    <label for="oldPw" class="col-sm-2 col-form-label">Old Password</label>
                    <div class="col-sm-10">
                        <input type="password" class="form-control" name="oldPw" id="oldPw" placeholder="Old Password">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="newPw" class="col-sm-2 col-form-label">New Password</label>
                    <div class="col-sm-10">
                        <input type="password" class="form-control" name="newPw" id="newPw" placeholder="New Password">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="confirmPw" class="col-sm-2 col-form-label">Confirm New Password</label>
                    <div class="col-sm-10">
                        <input type="password" class="form-control" name="confirmPw" id="confirmPw" placeholder="Confirm New Password">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-sm-10">
                        <button type="submit" class="btn btn-primary">Change Password</button>
                    </div>
                </div>
            </form>
        </div>
    `
}

function addAdmin() {
    profileDiv.innerHTML = `
        <div class="changePw">
            <form class="addAdmin" action="" method="post">
                <div class="form-group row">
                    <label for="username" class="col-sm-2 col-form-label">Name</label>
                    <div class="col-sm-10">
                        <input type="text" class="form-control" name="username" id="username" placeholder="Name" />
                    </div>
                </div>
                <div class="form-group row">
                    <label for="email" class="col-sm-2 col-form-label">E-mail</label>
                    <div class="col-sm-10">
                        <input type="email" class="form-control" name="email" id="email" placeholder="E-mail" />
                    </div>
                </div>
                <div class="form-group row">
                    <label for="password1" class="col-sm-2 col-form-label">Password</label>
                    <div class="col-sm-10">
                        <input type="password" class="form-control" name="password1" id="password1" placeholder="Password" />
                    </div>
                </div>
                <div class="form-group row">
                    <label for="password2" class="col-sm-2 col-form-label">Confirm Password</label>
                    <div class="col-sm-10">
                        <input type="password" class="form-control" name="password2" id="password2" placeholder="Password Confirmation" />
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-sm-10">
                        <button type="submit" class="btn btn-primary">Add Admin</button>
                    </div>
                </div>
            </form>
        </div>
    `
}

nameButton.addEventListener("click", changeName);
emailButton.addEventListener("click", changeEmail);
pwButton.addEventListener("click", pwChange);
adminButton.addEventListener("click", addAdmin);