import React from "react"

import { navigateTo } from "gatsby-link"

import Recaptcha from "react-google-recaptcha";
const RECAPTCHA_KEY = process.env.SITE_RECAPTCHA_KEY

function encode(data) {
    return Object.keys(data)
      .map(key => encodeURIComponent(key) + "=" + encodeURIComponent(data[key]))
      .join("&");
  }

class Contact extends React.Component {
    constructor(props) {
    super(props);
    this.state = {};
    }

    handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
    };

    handleRecaptcha = value => {
    this.setState({ "g-recaptcha-response": value });
    };

    handleSubmit = e => {
    e.preventDefault();
    const form = e.target;
    fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: encode({
        "form-name": form.getAttribute("name"),
        ...this.state
        })
    })
        .then(() => navigateTo(form.getAttribute("action")))
        .catch(error => alert(error));
    };

    render() {
        return (
            <div>
            <h3>Contact me</h3>
            <form
            name="contact-recaptcha"
            method="post"
            action="/thanks"
            data-netlify="true"
            data-netlify-recaptcha="true"
            onSubmit={this.handleSubmit}
            >
            <noscript>
                <p>This form won’t work with Javascript disabled</p>
            </noscript>
            <p>
                <label>
                Your name:<br />
                <input type="text" name="name" onChange={this.handleChange} />
                </label>
            </p>
            <p>
                <label>
                Your email:<br />
                <input type="email" name="email" onChange={this.handleChange} />
                </label>
            </p>
            <p>
                <label>
                Message:<br />
                <textarea name="message" onChange={this.handleChange} style={{display:'block', width:'80%', height:'200px'}}/>
                </label>
            </p>
            <Recaptcha
                ref="recaptcha"
                sitekey={RECAPTCHA_KEY}
                onChange={this.handleRecaptcha}
            />
            <br />
            <p>
                <button type="submit">Send</button>
            </p>
            </form>
                    <p>This site was built with <a href="https://www.gatsbyjs.org">Gatsby</a> and is based on the <a href="https://www.gatsbyjs.org/starters/gatsbyjs/gatsby-starter-blog/">Starter blog template</a> by <a href="https://twitter.com/kylemathews">Kyle Mathews</a>
    </p>
            </div>
        )
    }
    
}

export default Contact;