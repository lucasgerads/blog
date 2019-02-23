import React from "react"
import { graphql } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

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
        <h1>Contact</h1>
        <form
          name="contact"
          method="post"
          action="/thanks/"
          data-netlify="true"
          data-netlify-honeypot="bot-field"
          onSubmit={this.handleSubmit}
        >
          {/* The `form-name` hidden field is required to support form submissions without JavaScript */}
          <input type="hidden" name="form-name" value="contact" />
          <p hidden>
            <label>
              Don’t fill this out:{" "}
              <input name="bot-field" onChange={this.handleChange} />
            </label>
          </p>
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
