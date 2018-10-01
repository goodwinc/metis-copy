# Blogging with Hugo
There are all kinds of platforms for blogging that exist: Medium, Wordpress, Blogger, Tumblr ... (the list goes on). Typically, people will post their blogs on one of these options, and leave it at that. But, there are many benefits to having a personal blog that is built by and hosted all by you. You can do that using [Static Site Generators](https://www.staticgen.com/) like Jekyll, Hugo, and Next. This tutorial will talk specifically about how to make your blogging website using [Hugo](https://gohugo.io/).

The following steps should walk you through the process to building a decent blog. If you want to go straight to just using the Hugo documentation, check out the instruction [here](https://gohugo.io/hosting-and-deployment/hosting-on-github/#github-user-or-organization-pages).

## 1. Install Hugo
### Mac Users
First, make sure you have [Homebrew](https://brew.sh/) installed. Then, all you have to do to [install Hugo](https://gohugo.io/getting-started/quick-start/) is run a quick `brew install hugo` in the command line from your home directory.

### Non-Mac Users
Check the [Hugo Installation Guide](https://gohugo.io/getting-started/installing) guide for instructions for your operating system.

## 2. Setting Up Your Repositories
The first thing you need to do is set up your blog repository, and your site repository **on GitHub**. To do this:

1. Log into your GitHub account
2. Click the "Repositories (##)" tab at the top of the page, and then click "[Book Icon] New" on the upper right corner.
3. In the open box, name your blog repo (the name *blog* should work fine). Make this Public, and you don't need to add a README.
4. Click "Create Respository". This repository will contain all the content for your blog. Hugo
5. Back in your Repositories listing, click the "[Book Icon] New" icon again, to create your website repository.
6. This time, when you name the repository, you *need* to name it based on your GitHub account name. This repo should be named ***[YOUR-GITHUB-USERNAME].github.io***. So, for example, if your GitHub username is *JEddy92*, you'd name the repository JEddy92.github.io (ignore the link presentation on this Markdown file). Again, you don't need to add a README.
7. Click "Create Respository". This is the repository that contains the actual source code (HTML, CSS, etc.) for the webpage. Hugo *builds* this folder on your command before deploying it.

## 3. Setting Up Your Blog Framework, and Publishing
This is the fun part! Careful though, you just need to make sure that your folders are set up correctly.

1. Go to the [Hugo Themes Page](https://themes.gohugo.io/), and scroll through all the amazing themes and templates (you can use the 'Blog' link on the right hand side to filter your results). Test out the site with the 'Demo' link on each template, and pick one that you think is cooooool!
2. Click the 'Download' button from the template. This may take you to a GitHub, or it may just download the repository outright in a .zip folder. If it leads you to GitHub, just download the repository using the 'Clone or Download' icon on the repo it takes you to, and click 'Download Zip'. Then, move *the whole set* of folders and files (from within the unzipped folder) into your *blog* folder. You should have a directory that looks something like this:
```
~ home
    / [... whatever you folders are ...]
        / blog
            / archetypes
            / exampleSite
            / images
            / layouts
            / static
            / theme.toml
            / .gitignore
            / LICENSE.md
            / README.md
            / custom_config.json
```
3. The best way to build your site is to work with the *exampleSite* as a starting place. The *exampleSite* directory should look something like this:
```
[...]
/ exampleSite
    / content
    / data
    / layouts
    / static
    / config.toml
```
The idea here is to move the content of this example site into the main *blog* directory. You'll likely notice some repeats (e.g., *static*, *layouts*) between the *exampleSite* and the main *blog* directory. You want to take the union (e.g., if */exampleSite/static/* contains {*img* and *docs*}, and */blog/static/* contains {*css*, and *img*}, you want to have */blog/static/* contain {*docs*, *css*, and *img*}, where *img* contains the union of the two *img*s, in the same way).

Now, **delete the *exampleSite* directory**, and you also need to make sure to **add a */blog/public* directory**. It'll be empty for now. So, you're directory should look something like this:
```
~ home
    / [... whatever you folders are ...]
        / blog
            / archetypes
            / content
                / blog
                    post1.md
                    post2.md
                    ...
                / about
                    aboutme.md
            / data
            / images
            / layouts
                / partials
                ...
            / public
                [EMPTY]     # This is where Hugo eventually builds the site
            / static
                / style
                    style.css
                    ...
                ...
            / config.toml
            / custom_config.json
            / LICENSE.md
            / README.md
            / theme.toml
            / .gitignore    # This is hidden. Use Cmd+. to see these
```
4. Go into the command line, and navigate **into** `/blog` (i.e., the directory above). Run `hugo server` from the command line (*Note: If your theme uses yarn, or some other builder, to build the site, you need to run `yarn run build`, for instance, before running `hugo server`*). Now, you should see something like *"... available at https://localhost:1313"* as an out. You can navigate to that in your browser, and you should be able to see your site from there. I like to open up a partition of my screen for my IDE where I can edit code in the *blog* directory, and a partition for the localhost. That way, when I save in the IDE, I will see the updates show up on the browser (a sort of preview).

5. The files you want to update first are the *config.toml*, and the files in the */content* folder. Specifically, the information in the *config.toml* file are pretty self explanatory. Just update the metadata, and add pages where they are missing (if you have files corresponding to them). As for *content*, just copy/paste the markdown from the example site, and udpate the markdown file with your blog post content. Maintin the formatting of the top of the page, and update titles and names as need be.

```
# The top of a post or page should look like this
+++
title = "A Blog Post About Stuff"
description = "This is a blog post, about stuff. It is full of the stuff."
date = 2018-09-21T00:00:00Z     # <- This date must be in the past
author = "Leon Johnson"     # Doesn't NEED to match the config, it's whatever
+++

# You should have corresponding sections of the config for things like about pages

# This could be a section of the config at the bottom
[[menu.main]]
    name = "About"
    url = "/page/about/"
    weight = 3
```

Use the Hugo documentation on [file hierarchy](https://gohugo.io/content-management/organization/), and config.toml [configuration](https://gohugo.io/getting-started/configuration/) for more direction. Really, the Hugo site is going to be your best resource for all of this. It's all very self explanatory, but there are a few nuances.

6. Before building and deploying the site for the first time, run `git submodule add -b master git@github.com:<USERNAME>/<USERNAME>.github.io.git public` from the command line from **inside** the *blog* directory. The `<USERNAME>` is your GitHub username. So, if you're JEddy92, you'll run from the command line `git submodule add -b master git@github.com:JEddy92/JEddy92.github.io.git public`. **You only need to do this once.**

7. Lastly, copy paste the following into a script (basically, a raw text file), and save it **in the *blog* directory** as *deploy.sh*.
```
#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

# Go To Public folder
cd public
# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master

# Come Back up to the Project Root
cd ..
```

8. For this time and any other time that you're ready to deploy/publish your site after making changes, all you need to do is navigate into the *blog* directory, and run `./deploy.sh "Your optional commit message"`. The message is required, so try to make it somewhat descriptive. After that, wait a few minutes and your site should be up and running! If not, check out the [Hugo Troubleshooting page](https://gohugo.io/troubleshooting/), or just use good ole Google!

9. The last step here is to double up your posting onto [Medium.com](https://medium.com/). If you don't already have an account, make sure to make one and ensure that your bio and information are up to date. You can click your little picture on the upper right corner, and go to "Stories", then use the "Import a Story" function on the upper right corner. Paste the link to your blog post, and then use the Medium user interface to clean up the post that it tried to copy. It's a good idea to have your post in both places, and it's also a good idea to ensure you advertise your post on LinkedIn and other sites like that!

10. Let the job offers flow in!


