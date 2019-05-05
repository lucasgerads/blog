import React from "react"
import { graphql } from "gatsby"

import { navigateTo } from "gatsby-link";

import Layout from "../components/layout"
import SEO from "../components/seo"
import Contact from "../components/contact"

import Recaptcha from "react-google-recaptcha";
const RECAPTCHA_KEY = process.env.SITE_RECAPTCHA_KEY;

function encode(data) {
  return Object.keys(data)
    .map(key => encodeURIComponent(key) + "=" + encodeURIComponent(data[key]))
    .join("&");
}

class About extends React.Component {
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
    const { data } = this.props
    const siteTitle = data.site.siteMetadata.title
    const bio = this.props.data.markdownRemark
   
    console.log(bio)

    return (
      <Layout location={this.props.location} title={siteTitle}>
        <SEO title="About" />
         <div dangerouslySetInnerHTML={{ __html : bio.html }} /> 
         <Contact />
         </Layout>
    )
  }
}

export default About 

export const pageQuery = graphql`
  query {
    site {
        siteMetadata {
          title
        }
      }
      markdownRemark (fields: { slug: { eq: "/bio/" } }) {
        html
    } 
  } 
`
