/** @type {import('next').NextConfig} */

const isGithubActions = process.env.GITHUB_ACTIONS || false

let assetPrefix = ''
let basePath = '/'

if (isGithubActions) {
  const repo = process.env.GITHUB_REPOSITORY.replace(/.*?\//, '')

  assetPrefix = `/${repo}/`
  basePath = `/${repo}`
}


const nextConfig = {
  experimental: {
    appDir: true,
  },
  assetPrefix: assetPrefix,
  basePath: basePath,
  output: 'export',
  images: {
    loader: 'imgix',
    path: 'the "domain" of your Imigix source',
  },
}


module.exports = nextConfig

