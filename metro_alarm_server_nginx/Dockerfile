FROM nginx:1.23.3-alpine


RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/
COPY metro_alarm_server.crt /etc/nginx
COPY metro_alarm_server.key /etc/nginx

CMD ["nginx", "-g", "daemon off;"]