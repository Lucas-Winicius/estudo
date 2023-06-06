type User = {
  username: string;
  password: string;
};
type VerifyUserFn = (user: User, sentValue: User) => boolean;

const verifyUser: VerifyUserFn = (user, sentValue) => {
  return (
    user.username === sentValue.username && user.password === sentValue.password
  );
};

const dbUser: User = {
  username: "Lucas_W",
  password: "12345678",
};

const sendUser: User = {
  username: "Lucas_W",
  password: "12345678",
};

const loggedIn = verifyUser(dbUser, sendUser);
console.log(loggedIn);
