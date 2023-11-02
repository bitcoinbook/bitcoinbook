<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:h="http://www.w3.org/1999/xhtml"
                xmlns="http://www.w3.org/1999/xhtml"
                exclude-result-prefixes="h">

  <!-- Add title heading elements for different admonition types that do not already have headings in markup -->
  <xsl:param name="add.title.heading.for.admonitions" select="1"/>  

  <!-- Drop @width attributes from table headers if present -->
  <xsl:template match="h:th/@width"/>

  <!-- Drop @width attributes from images if present -->
  <xsl:template match="h:img/@width"/>

 <!-- Drop @alt attribute content from images if present -->
  <xsl:template match="h:img/@alt">
    <xsl:attribute name="alt"/>
  </xsl:template>
</xsl:stylesheet>
