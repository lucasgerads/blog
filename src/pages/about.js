import React from "react"
import { graphql } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

import Recaptcha from "react-google-recaptcha";
const RECAPTCHA_KEY = process.env.SITE_RECAPTCHA_KEY;

class NotFoundPage extends React.Component {
  render() {
    const { data } = this.props
    const siteTitle = data.site.siteMetadata.title

    return (
      <Layout location={this.props.location} title={siteTitle}>
        <SEO title="About" />
        <h1>About me</h1>
        <p> 
          I am interested in and write about, in descending order of expertise:
          technology, business, science, entrepreneurship, politics, and life. All
          opinions expressed on this blog are my own.  
        </p>
         <p> 
          I run the company <a href="http://aixcon.de">Aixcon PowerSystems GmbH</a> in Stolberg (Rhld.),
          Germany, spending my days building power electronics and automation for
          various applications such as welding, coating and material treatment. My
          lovely life partner Lydia helps me edit my posts. </p>        
        <div>
        <h3>reCAPTCHA 2</h3>
        <form
          name="contact-recaptcha"
          method="post"
          action="/thanks/"
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
              <textarea name="message" onChange={this.handleChange} />
            </label>
          </p>
          <Recaptcha
            ref="recaptcha"
            sitekey={RECAPTCHA_KEY}
            onChange={this.handleRecaptcha}
          />
          <p>
            <button type="submit">Send</button>
          </p>
        </form>
      </div> 
      
                <p>This site was built with <a href="https://www.gatsbyjs.org">Gatsby</a> and is based on the <a href="https://www.gatsbyjs.org/starters/gatsbyjs/gatsby-starter-blog/">Starter blog template</a> by <a href="https://twitter.com/kylemathews">Kyle Mathews</a>
</p>
      </Layout>
    )
  }
}

export default NotFoundPage

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`
