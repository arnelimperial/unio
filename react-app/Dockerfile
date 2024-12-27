FROM node:22.12.0-alpine

RUN apk add --no-cache yarn

WORKDIR /app

RUN adduser -D myuser

RUN chown -R myuser:myuser /app

COPY package.json yarn.lock ./

RUN yarn install 

ENV NODE_ENV=development

ENV PATH=/app/node_modules/.bin:$PATH

COPY --chown=myuser:myuser . .

EXPOSE 5173

USER myuser

CMD ["yarn", "dev"]