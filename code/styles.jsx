import styled from "styled-components";
import logoRed from "resources/logo.png";
import nicknameprofileimg from "resources/NicknameProfileImg.png";
import notifications from "resources/notifications.png";
import email from "resources/email.png";
import LoginProfileIcon from "resources/profile_icon_183860.svg";
import menuIcon from './menu.png';

export const Container = styled.div`
  width: 100%;
  max-width: 1920px;
  height: 103px;
  display: flex;
  justify-content: center;
  align-items: center; 
  list-style: none;

  @media screen and (max-width: 800px) {
    flex-direction: column;
    /* align-items: center; */
  }
`;

export const Header = styled.div`
    display: flex;
    list-style: none;
    /* margin-top: 60px; */

    .navbar{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    @media screen and (max-width: 800px) {
        flex-direction: column;
        /* display: none; */

        .header-ul {
            flex-direction: column;
            margin-top: 140px;
        }

        .navbar{
            display: ${(props) => (props.istoggled ? "block" : "none")};
            flex-direction: column;
            align-items: flex-start;
            width: 100%;
            height: 500px;
            z-index: 2;
            background-color: black;
            /* flex-direction: column; */
            /* align-items: flex-start; */
        }
    }
    
`;

export const Menu = styled.img.attrs({
    src: menuIcon,
})`
    width: 60px;
    height: 70px;
    display: none;
    /* position: absolute; */
    /* right: 30px; */
    cursor: pointer;

    @media screen and (max-width: 800px) {
        /* flex-direction: column; */
        /* position: absolute; */
        /* right: 32px; */
        display: block;
    }
`;

export const Logo = styled.img.attrs({
  src: logoRed,
})`
  width: 99px;
  height: 99px;
  margin-left: 27px;

  @media screen and (max-width: 800px) {
    /* display: none; */
    position: absolute;
    left: 27px;
  }
`;

export const Play = styled.button`
  width: 159px;
  height: 43px;
  background: transparent linear-gradient(270deg, #ff8900 0%, #ffffff 100%) 0%
    0% no-repeat padding-box;
  border-radius: 0px 22px 22px 0px;
  opacity: 1;
  cursor: pointer;
  border: 0;
  outline: 0;
  @media screen and (max-width: 800px) {
    flex-direction: column;
    /* color: black;
    background: none; */

  }
`;

export const PlayText = styled.div`
  font: normal normal 900 16px/19px Pretendard;
  letter-spacing: 0px;
  color: #ffffff;
  opacity: 1;
  // margin-top: 1px;
  margin-left: 94px;

  @media screen and (max-width: 800px) {
    /* color: black; */
  }
`;

export const Learn = styled.button`
  background: transparent linear-gradient(270deg, #8800ff 0%, #ffffff 100%) 0%
    0% no-repeat padding-box;
  border-radius: 0px 22px 22px 0px;
  opacity: 1;
  width: 159px;
  height: 43px;
  cursor: pointer;
  border: 0;
  outline: 0;
`;
export const LearnText = styled.div`
  font: normal normal 900 16px/19px Pretendard;
  letter-spacing: 0px;
  color: #ffffff;
  opacity: 1;
  // margin-top: 1px;
  margin-left: 87px;
`;
export const Make = styled.button`
  background: transparent linear-gradient(270deg, #0062ff 0%, #ffffff 100%) 0%
    0% no-repeat padding-box;
  border-radius: 0px 22px 22px 0px;
  opacity: 1;
  width: 159px;
  height: 43px;
  cursor: pointer;
  border: 0;
  outline: 0;
`;
export const MakeText = styled.div`
  font: normal normal 900 16px/19px Pretendard;
  letter-spacing: 0px;
  color: #ffffff;
  opacity: 1;
  // margin-top: 1px;
  margin-left: 87px;
`;
export const SearchExp = styled.input`
  background: #848484 0% 0% no-repeat padding-box;
  border-radius: 22px;
  opacity: 1;
  width: 740px;
  height: 43px;
  cursor: pointer;
  border: 0;
  outline: 0;
  // margin-left: 9px;
  position: relative;
  z-index: 1;
  box-sizing: border-box;
  padding-left: 35px;
  font: normal normal 500 16px/19px Pretendard;

  @media screen and (max-width: 800px) {
    display: none;
  }
`;


export const SearchExpText = styled.div`
  font: normal normal 900 16px/19px Pretendard;
  letter-spacing: 0px;
  color: #ffffff;
  text-align: right;
  position: absolute;
  right: 23px;
  top: 11px;
  z-index: 2;
  cursor: default;
  opacity: ${(prop) => prop.opacity || 1};

  @media screen and (max-width: 800px) {
    display: none;
  }
`;

export const Register = styled.button`
  width: 156px;
  height: 42px;
  border-radius: 22px;
  background: #ff181b 0% 0% no-repeat padding-box;
  opacity: 1;
  cursor: pointer;
  border: 0;
  outline: 0;
  margin-right: 4px;

  @media screen and (max-width: 800px) {
    display: none;
  }
`;

export const RegisterText = styled.div`
  font: normal normal 900 18px/21px Pretendard;
  letter-spacing: 0px;
  color: #ffffff;
  position: relative;
  text-align: center;
  cursor: pointer;
  margin-right: 0px;

  @media screen and (max-width: 800px) {
    display: none;
  }
`;

export const Login = styled.button`
  width: 156px;
  height: 42px;
  border-radius: 22px;
  background: #848484 0% 0% no-repeat padding-box;
  opacity: 1;
  cursor: pointer;
  border: 0;
  outline: 0;
  margin-right: 27px;
  position: relative;

  @media screen and (max-width: 800px) {
    display: none;
  }
`;

export const LoginText = styled.div`
  font: normal normal 900 18px/21px Pretendard;
  letter-spacing: 0px;
  color: #ffffff;
  opacity: 1;
  position: relative;
  text-align: center;
  cursor: pointer;
  margin-right: 0px;
  margin-left: 21.1px;

  @media screen and (max-width: 800px) {
    display: none;
  }
`;

export const LoginIcon = styled.div`
  width: 20px;
  height: 25px;
  position: absolute;
  top: 9.75px;
  left: 32.2px;
  // background-color: white;
  background-image: url(${LoginProfileIcon});
  background-size: cover;
  background-position: center center;
`;
export const RegistBox = styled.div`
  display: flex;
  position: relative;
  font-size: 16px;
  margin-left: auto;
  margin-right: 27px;
`;
export const NotificationIcon = styled.img.attrs({
  src: notifications,
})`
  width: 44.09px;
  height: 44.09px;
  margin-left: 66.69px;
`;
export const EmailIcon = styled.img.attrs({
  src: email,
})`
  width: 44px;
  height: 45px;
  margin-left: 33.22px;
`;
export const Nickname = styled.button`
  width: 156px;
  height: 42px;
  border-radius: 22px;
  background: #848484 0% 0% no-repeat padding-box;
  opacity: 1;
  cursor: pointer;
  border: 0;
  outline: 0;
  // margin-right: 27px;
  position: relative;
`;
export const NicknameIcon = styled.img.attrs({
  // src: nicknameprofileimg,
})`
  width: 43px;
  height: 43px;
  position: absolute;
  top: 0px;
  left: 0px;
  // background-color: white;
  border-radius: 100%;
  background-image: url(${(props) => props.src || nicknameprofileimg});
`;
export const NicknameText = styled.div`
  font: normal normal 900 18px/21px Pretendard;
  letter-spacing: 0px;
  color: #ffffff;
  opacity: 1;
  position: relative;
  text-align: center;
  cursor: pointer;
  margin-right: 0px;
  margin-left: 31.38px;
`;