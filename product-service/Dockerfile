# Step 1: Choose a lightweight base image with Node.js pre-installed
FROM node:20-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy package files first to optimize Docker caching
COPY package*.json ./

# Step 4: Install only production dependencies
RUN npm install --only=production

# Step 5: Copy the rest of the application source code
COPY app.js .

# Step 6: Inform Docker that the container listens on port 5001 at runtime
EXPOSE 5001

# Step 7: Define the command to run the application
CMD ["npm", "start"]
