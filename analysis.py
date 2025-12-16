import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime
from io import BytesIO
import random
import warnings
warnings.filterwarnings("ignore")

# Page Configuration
st.set_page_config(
    page_title="Data Analytics Platform",
    page_icon="📊",
    layout="wide"
)

# Initialize language in session state
if 'language' not in st.session_state:
    st.session_state.language = 'en'

# Language translations
translations = {
    'en': {
        'title': 'Data Analytics Platform',
        'subtitle': 'Complete Statistical Analysis Solution for Researchers',
        'welcome': 'Welcome!',
        'welcome_text': 'Empowering researchers with intuitive statistical analysis tools. Transform your data into meaningful insights with our comprehensive platform.',
        'core_features': 'Core Features',
        'descriptive_stats': 'Descriptive Statistics',
        'descriptive_desc': 'Mean, median, variance, etc.',
        'spearman': 'Spearman Correlation',
        'spearman_desc': 'For ordinal data analysis',
        'data_viz': 'Data Visualization',
        'data_viz_desc': 'Interactive charts & plots',
        'regression': 'Regression Analysis',
        'regression_desc': 'Trend lines & predictions',
        'stat_testing': 'Statistical Testing',
        'stat_testing_desc': 'p-values & significance',
        'corr_matrix': 'Correlation Matrix',
        'corr_matrix_desc': 'Multi-variable relationships',
        'footer': '© 2024 Data Analytics Platform | Group 3 Project',
        'footer_sub': 'Advanced Statistical Analysis with Spearman Correlation',
        'platform_title': 'Advanced Statistical Analysis Platform',
        'platform_subtitle': 'Comprehensive Data Analysis Solution • Group 3 Project • Professional Analytics Tool',
        'objectives': 'Project Objectives',
        'global_access': 'Global Accessibility',
        'global_text_1': 'Develop an intuitive web-based platform for statistical analysis accessible to users of all skill levels',
        'global_text_2': 'Support 12 international languages to ensure global accessibility and usability',
        'comprehensive': 'Comprehensive Analysis',
        'comp_text_1': 'Implement comprehensive descriptive statistics tools for data exploration and summary',
        'comp_text_2': 'Provide advanced correlation analysis using Spearman method for ordinal data',
        'tech_stack': 'Technology Stack',
        'tech_text': 'Our platform is built on a modern technology stack that ensures reliability, performance, and scalability.',
        'our_team': 'Our Team',
        'team_text': 'Meet the talented team behind this project.',
        'about_analysis': 'About the Analysis',
        'about_text': 'This application performs two major statistical procedures:',
        'descriptive_analysis': 'Descriptive Analysis - summarizes characteristics of variables',
        'association_analysis': 'Association Analysis (Spearman Correlation) - evaluates relationships',
        'desc_analysis_title': '1) Descriptive Analysis',
        'basic_stats_title': 'Basic Statistics:',
        'basic_stats_text': 'Mean, Median, Mode, Min/Max, Standard Deviation',
        'distribution_title': 'Distribution & Frequency:',
        'distribution_text': 'Histograms, Bar charts, Frequency tables',
        'summaries_title': 'Variable Summaries:',
        'summaries_text': 'Boxplots, Quartiles',
        'assoc_analysis_title': '2) Association Analysis',
        'spearman_coef': 'Spearman Correlation Coefficient (ρ): Measures strength and direction',
        'p_value': 'p-value: Determines statistical significance',
        'visualizations': 'Visualizations: Scatter plots with trend lines',
        'interpretations': 'Interpretations: Automatic classification of strength',
        'program_obj': 'Program Objectives',
        'obj_1': 'Provide complete descriptive statistics',
        'obj_2': 'Display interactive visualizations',
        'obj_3': 'Measure associations using Spearman correlation',
        'obj_4': 'Generate interpretable insights for academic reports',
        'obj_5': 'Allow custom data upload for flexibility',
        'upload_dataset': 'Upload Dataset',
        'accepted_formats': 'Accepted formats: CSV, Excel (.xlsx, .xls)',
        'dataset_loaded': 'Dataset loaded successfully',
        'rows': 'Rows',
        'columns': 'Columns',
        'size': 'Size',
        'variable_selection': 'Variable Selection',
        'select_x': 'Select X variables',
        'select_y': 'Select Y variables',
        'create_composite': 'Create composite scores',
        'run_analysis': 'Run Full Analysis',
        'desc_analysis': 'Descriptive Analysis',
        'variable': 'Variable',
        'count': 'Count',
        'mean': 'Mean',
        'median': 'Median',
        'min': 'Min',
        'max': 'Max',
        'std_dev': 'Std Dev',
        'variance': 'Variance',
        'range': 'Range',
        'key_insights': 'Key Insights:',
        'central_tendency': 'Central Tendency',
        'spread': 'Spread',
        'likert_detected': 'Likert Scale Detected',
        'likert_text': 'Suitable for non-parametric testing.',
        'frequency_dist': 'Frequency Distribution',
        'category': 'Category',
        'frequency': 'Frequency',
        'percentage': 'Percentage (%)',
        'normality_test': 'Normality Testing',
        'normal': 'Normal',
        'non_normal': 'Non-Normal',
        'method': 'Method',
        'association': 'Association Analysis',
        'pearson': 'Pearson Correlation',
        'spearman_rank': 'Spearman Rank Correlation',
        'coefficient': 'Coefficient',
        'strength': 'Strength',
        'direction': 'Direction',
        'positive': 'Positive',
        'negative': 'Negative',
        'significance': 'Significance',
        'yes': 'Yes',
        'no': 'No',
        'interpretation': 'Interpretation:',
        'relationship': 'relationship',
        'correlation': 'correlation',
        'significant': 'Significant',
        'not_significant': 'Not Significant',
        'note': 'Note',
        'causation_note': 'Correlation ≠ Causation',
        'conclusion': 'Conclusion',
        'key_findings': 'Key Findings:',
        'finding_1': 'Descriptive analysis revealed meaningful patterns',
        'finding_2': 'Composite scores improve reliability',
        'finding_3': 'Association analysis shows interpretable relationships',
        'finding_4': 'Results suitable for academic reporting',
        'understanding_corr': 'Understanding Correlation Methods',
        'pearson_corr': 'Pearson Correlation',
        'spearman_corr': 'Spearman Rank Correlation (ρ)',
        'purpose': 'Purpose:',
        'requirements': 'Requirements:',
        'when_use': 'When to use:',
        'method_calc': 'Method:',
        'formula': 'Formula:',
        'range_val': 'Range:',
        'sensitivity': 'Sensitivity:',
        'advantage': 'Advantage:',
        'perfect_for': 'Perfect for:',
        
        # Pearson descriptions
        'pearson_purpose': 'Measures linear relationships between continuous variables',
        'pearson_req': 'Assumes normal distribution, interval/ratio data, linear relationship',
        'pearson_when': 'When both variables are normally distributed and relationship is linear',
        'pearson_formula': 'r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)²Σ(yi - ȳ)²]',
        'pearson_range': '-1 to +1 (perfect negative to perfect positive correlation)',
        'pearson_sensitivity': 'Highly sensitive to outliers and extreme values',
        
        # Spearman descriptions
        'spearman_purpose': 'Measures monotonic relationships (not necessarily linear)',
        'spearman_req': 'Works with ordinal, interval, or ratio data; non-parametric',
        'spearman_when': 'When data is not normally distributed, contains outliers, or involves ordinal data (like Likert scales 1-5)',
        'spearman_method': 'Uses rank-based calculation instead of raw values',
        'spearman_advantage': 'More robust to outliers and non-normal distributions',
        'spearman_perfect': 'Survey data with Likert scales, ranked preferences, ordinal measurements',
        
        # Table
        'key_diff': 'Key Differences: Pearson vs Spearman',
        'aspect': 'Aspect',
        'data_type': 'Data Type',
        'relationship_type': 'Relationship Type',
        'distribution': 'Distribution',
        'outliers': 'Outliers',
        'likert_scales': 'Likert Scales (1-5)',
        'calculation': 'Calculation',
        'best_app': 'Best Application',
        
        # Table values
        'continuous': 'Continuous (interval/ratio)',
        'ordinal_continuous': 'Ordinal or continuous',
        'linear_only': 'Linear only',
        'monotonic': 'Monotonic (any consistent direction)',
        'requires_norm': 'Requires normality',
        'no_assumption': 'No distribution assumption needed',
        'highly_sensitive': 'Highly sensitive',
        'robust_resistant': 'Robust and resistant',
        'not_recommended': 'Not recommended',
        'ideal_choice': 'Ideal choice',
        'uses_raw': 'Uses raw data values',
        'uses_ranked': 'Uses ranked data',
        'experimental': 'Experimental data, measurements',
        'survey_research': 'Survey research, questionnaires',
        
        # When to use
        'when_use_which': 'When to Use Which Method?',
        'use_pearson_when': 'Use Pearson when:',
        'use_spearman_when': 'Use Spearman when:',
        'normal_dist': 'Data is normally distributed',
        'linear_rel': 'Relationship is linear',
        'vars_continuous': 'Variables are continuous',
        'no_outliers': 'No significant outliers',
        'ordinal_data': 'Data is ordinal (Likert scales)',
        'non_normal': 'Non-normal distribution',
        'presence_outliers': 'Presence of outliers',
        'monotonic_not_linear': 'Monotonic but not linear',

        'pdf_title': 'STATISTICAL ANALYSIS REPORT',
        'pdf_report_info': 'Report Information',
        'pdf_generated': 'Generated',
        'pdf_total_resp': 'Total Respondents',
        'pdf_x_vars': 'X Variables',
        'pdf_y_vars': 'Y Variables',
        'pdf_exec_summary': 'EXECUTIVE SUMMARY',
        'pdf_exec_text_1': 'This comprehensive statistical analysis report presents findings from survey data with',
        'pdf_exec_text_2': 'respondents. The analysis reveals a',
        'pdf_exec_text_3': 'relationship between X and Y variables (correlation coefficient =',
        'pdf_exec_text_4': 'p-value =',
        'pdf_exec_text_5': 'The relationship is',
        'pdf_statistically_sig': 'statistically significant',
        'pdf_not_statistically_sig': 'not statistically significant',
        'pdf_exec_text_6': 'at α = 0.05 level. The chosen method',
        'pdf_exec_text_7': 'was selected based on normality testing of the data distribution.',
        'pdf_desc_stats': 'DESCRIPTIVE STATISTICS',
        'pdf_variable': 'Variable:',
        'pdf_statistic': 'Statistic',
        'pdf_value': 'Value',
        'pdf_distribution': 'Distribution:',
        'pdf_normality_test': 'NORMALITY TESTING',
        'pdf_normality_text': 'Shapiro-Wilk test was conducted to assess the normality of data distribution:',
        'pdf_interpretation_col': 'Interpretation',
        'pdf_data_follows': 'Data follows normal distribution',
        'pdf_data_not_follows': 'Data does not follow normal distribution',
        'pdf_selected_method': 'Selected Method:',
        'pdf_method_text_1': 'Based on the normality test results,',
        'pdf_method_text_2': 'was selected as the appropriate correlation analysis method.',
        'pdf_pearson_suitable': 'Pearson correlation is suitable when both variables follow normal distribution.',
        'pdf_spearman_suitable': 'Spearman correlation is more robust for non-normal distributions and ordinal data.',
        'pdf_corr_analysis': 'CORRELATION ANALYSIS',
        'pdf_metric': 'Metric',
        'pdf_interp': 'Interpretation',
        'pdf_method_used': 'Statistical method used',
        'pdf_relationship': 'relationship',
        'pdf_sample_size': 'Sample Size',
        'pdf_num_obs': 'Number of observations',
        'pdf_scatter_plot': 'Scatter Plot with Trend Line:',
        'pdf_trend_line': 'Trend Line',
        'pdf_interpretation': 'INTERPRETATION',
        'pdf_key_findings': 'The correlation analysis reveals the following key findings:',
        'pdf_strength_rel': 'Strength of Relationship:',
        'pdf_strength_text_1': 'The correlation coefficient of r =',
        'pdf_strength_text_2': 'indicates a',
        'pdf_strength_text_3': 'relationship between the variables. This suggests that',
        'pdf_substantial': 'there is a substantial association',
        'pdf_moderate': 'there is a moderate to weak association',
        'pdf_between_vars': 'between X and Y variables.',
        'pdf_direction_rel': 'Direction of Relationship:',
        'pdf_direction_text_1': 'The',
        'pdf_direction_text_2': 'correlation coefficient indicates that as X increases, Y tends to',
        'pdf_increase': 'increase as well',
        'pdf_decrease': 'decrease',
        'pdf_direction_text_3': 'This',
        'pdf_direct': 'direct',
        'pdf_inverse': 'inverse',
        'pdf_direction_text_4': 'relationship',
        'pdf_same_direction': 'suggests both variables move in the same direction',
        'pdf_opposite_direction': 'suggests the variables move in opposite directions',
        'pdf_stat_sig': 'Statistical Significance:',
        'pdf_sig_text_1': 'With a p-value of',
        'pdf_sig_text_2': 'the relationship is',
        'pdf_sig_text_3': 'This means',
        'pdf_reject_null': 'we can reject the null hypothesis and conclude that the observed correlation is unlikely due to chance',
        'pdf_cannot_reject': 'we cannot reject the null hypothesis, and the observed correlation may be due to random variation',
        'pdf_important_note': 'Important Note:',
        'pdf_causation': 'Correlation does not imply causation. While we observe',
        'pdf_sig_association': 'a significant association',
        'pdf_an_association': 'an association',
        'pdf_causation_text': 'between variables, this analysis alone cannot determine if one variable causes changes in the other.',
        'pdf_conclusion': 'CONCLUSION',
        'pdf_summary': 'Summary of Key Findings:',
        'pdf_desc_analysis_sum': 'Descriptive Analysis:',
        'pdf_desc_text': 'Successfully analyzed',
        'pdf_desc_text_2': 'variables, revealing meaningful patterns in the data distribution.',
        'pdf_composite': 'Composite Scores:',
        'pdf_composite_text': 'Created reliable aggregate measures (X_total and Y_total) that improve measurement reliability and reduce random error.',
        'pdf_corr_analysis_sum': 'Correlation Analysis:',
        'pdf_corr_text_1': 'Found a',
        'pdf_corr_text_2': 'that is',
        'pdf_corr_text_3': 'at the 0.05 level.',
        'pdf_method_rigor': 'Methodological Rigor:',
        'pdf_method_text': 'Applied appropriate statistical methods',
        'pdf_method_text_2': 'based on data distribution characteristics, ensuring valid and reliable results.',
        'pdf_academic': 'Academic Reporting:',
        'pdf_academic_text': 'Results are suitable for inclusion in academic papers, theses, and research reports with proper citation of methods and limitations.',
        'pdf_recommendations': 'Recommendations:',
        'pdf_rec_1': 'Consider conducting additional analyses to explore potential confounding variables',
        'pdf_rec_2': 'Examine subgroup differences if applicable to your research context',
        'pdf_rec_3': 'Replicate findings with independent samples to validate results',
        'pdf_rec_4': 'Consider qualitative methods to understand the mechanisms behind observed relationships',
        'pdf_footer': 'Report generated by Data Analytics Platform | © 2024 | Generated on',
        'pdf_download_btn': 'Download Complete Analysis Report with Charts (PDF)',
        'pdf_success': 'PDF report with all charts generated successfully!',
        'pdf_includes': 'This report includes: Executive Summary, Descriptive Statistics with Charts, Normality Tests, Correlation Analysis with Scatter Plot, Detailed Interpretation, and Conclusions.',
    },
    'id': {
        'title': 'Platform Analitik Data',
        'subtitle': 'Solusi Analisis Statistik Lengkap untuk Peneliti',
        'welcome': 'Selamat Datang!',
        'welcome_text': 'Memberdayakan peneliti dengan alat analisis statistik yang intuitif. Ubah data Anda menjadi wawasan yang bermakna dengan platform komprehensif kami.',
        'core_features': 'Fitur Utama',
        'descriptive_stats': 'Statistik Deskriptif',
        'descriptive_desc': 'Mean, median, varians, dll.',
        'spearman': 'Korelasi Spearman',
        'spearman_desc': 'Untuk analisis data ordinal',
        'data_viz': 'Visualisasi Data',
        'data_viz_desc': 'Grafik & plot interaktif',
        'regression': 'Analisis Regresi',
        'regression_desc': 'Garis tren & prediksi',
        'stat_testing': 'Pengujian Statistik',
        'stat_testing_desc': 'Nilai-p & signifikansi',
        'corr_matrix': 'Matriks Korelasi',
        'corr_matrix_desc': 'Hubungan multi-variabel',
        'footer': '© 2024 Platform Analitik Data | Proyek Kelompok 3',
        'footer_sub': 'Analisis Statistik Lanjutan dengan Korelasi Spearman',
        'platform_title': 'Platform Analisis Statistik Lanjutan',
        'platform_subtitle': 'Solusi Analisis Data Komprehensif • Proyek Kelompok 3 • Alat Analitik Profesional',
        'objectives': 'Tujuan Proyek',
        'global_access': 'Aksesibilitas Global',
        'global_text_1': 'Mengembangkan platform berbasis web yang intuitif untuk analisis statistik yang dapat diakses oleh pengguna dari semua tingkat keahlian',
        'global_text_2': 'Mendukung 12 bahasa internasional untuk memastikan aksesibilitas dan kegunaan global',
        'comprehensive': 'Analisis Komprehensif',
        'comp_text_1': 'Menerapkan alat statistik deskriptif yang komprehensif untuk eksplorasi dan ringkasan data',
        'comp_text_2': 'Menyediakan analisis korelasi lanjutan menggunakan metode Spearman untuk data ordinal',
        'tech_stack': 'Teknologi',
        'tech_text': 'Platform kami dibangun dengan teknologi modern yang menjamin keandalan, performa, dan skalabilitas.',
        'our_team': 'Tim Kami',
        'team_text': 'Kenali tim berbakat di balik proyek ini.',
        'about_analysis': 'Tentang Analisis',
        'about_text': 'Aplikasi ini melakukan dua prosedur statistik utama:',
        'descriptive_analysis': 'Analisis Deskriptif - merangkum karakteristik variabel',
        'association_analysis': 'Analisis Asosiasi (Korelasi Spearman) - mengevaluasi hubungan',
        'desc_analysis_title': '1) Analisis Deskriptif',
        'basic_stats_title': 'Statistik Dasar:',
        'basic_stats_text': 'Mean, Median, Modus, Min/Maks, Deviasi Standar',
        'distribution_title': 'Distribusi & Frekuensi:',
        'distribution_text': 'Histogram, Diagram batang, Tabel frekuensi',
        'summaries_title': 'Ringkasan Variabel:',
        'summaries_text': 'Boxplot, Kuartil',
        'assoc_analysis_title': '2) Analisis Asosiasi',
        'spearman_coef': 'Koefisien Korelasi Spearman (ρ): Mengukur kekuatan dan arah',
        'p_value': 'Nilai-p: Menentukan signifikansi statistik',
        'visualizations': 'Visualisasi: Diagram sebar dengan garis tren',
        'interpretations': 'Interpretasi: Klasifikasi kekuatan otomatis',
        'program_obj': 'Tujuan Program',
        'obj_1': 'Menyediakan statistik deskriptif lengkap',
        'obj_2': 'Menampilkan visualisasi interaktif',
        'obj_3': 'Mengukur asosiasi menggunakan korelasi Spearman',
        'obj_4': 'Menghasilkan wawasan yang dapat diinterpretasi untuk laporan akademik',
        'obj_5': 'Memungkinkan unggah data kustom untuk fleksibilitas',
        'upload_dataset': 'Unggah Dataset',
        'accepted_formats': 'Format diterima: CSV, Excel (.xlsx, .xls)',
        'dataset_loaded': 'Dataset berhasil dimuat',
        'rows': 'Baris',
        'columns': 'Kolom',
        'size': 'Ukuran',
        'variable_selection': 'Pemilihan Variabel',
        'select_x': 'Pilih variabel X',
        'select_y': 'Pilih variabel Y',
        'create_composite': 'Buat skor komposit',
        'run_analysis': 'Jalankan Analisis Lengkap',
        'desc_analysis': 'Analisis Deskriptif',
        'variable': 'Variabel',
        'count': 'Jumlah',
        'mean': 'Rata-rata',
        'median': 'Median',
        'min': 'Min',
        'max': 'Maks',
        'std_dev': 'Dev Std',
        'variance': 'Varians',
        'range': 'Rentang',
        'key_insights': 'Wawasan Utama:',
        'central_tendency': 'Tendensi Sentral',
        'spread': 'Sebaran',
        'likert_detected': 'Skala Likert Terdeteksi',
        'likert_text': 'Cocok untuk pengujian non-parametrik.',
        'frequency_dist': 'Distribusi Frekuensi',
        'category': 'Kategori',
        'frequency': 'Frekuensi',
        'percentage': 'Persentase (%)',
        'normality_test': 'Uji Normalitas',
        'normal': 'Normal',
        'non_normal': 'Tidak Normal',
        'method': 'Metode',
        'association': 'Analisis Asosiasi',
        'pearson': 'Korelasi Pearson',
        'spearman_rank': 'Korelasi Peringkat Spearman',
        'coefficient': 'Koefisien',
        'strength': 'Kekuatan',
        'direction': 'Arah',
        'positive': 'Positif',
        'negative': 'Negatif',
        'significance': 'Signifikansi',
        'yes': 'Ya',
        'no': 'Tidak',
        'interpretation': 'Interpretasi:',
        'relationship': 'hubungan',
        'correlation': 'korelasi',
        'significant': 'Signifikan',
        'not_significant': 'Tidak Signifikan',
        'note': 'Catatan',
        'causation_note': 'Korelasi ≠ Kausalitas',
        'conclusion': 'Kesimpulan',
        'key_findings': 'Temuan Utama:',
        'finding_1': 'Analisis deskriptif mengungkapkan pola bermakna',
        'finding_2': 'Skor komposit meningkatkan reliabilitas',
        'finding_3': 'Analisis asosiasi menunjukkan hubungan yang dapat diinterpretasi',
        'finding_4': 'Hasil cocok untuk pelaporan akademik',
        'understanding_corr': 'Memahami Metode Korelasi',
        'pearson_corr': 'Korelasi Pearson',
        'spearman_corr': 'Korelasi Peringkat Spearman (ρ)',
        'purpose': 'Tujuan:',
        'requirements': 'Persyaratan:',
        'when_use': 'Kapan digunakan:',
        'method_calc': 'Metode:',
        'formula': 'Rumus:',
        'range_val': 'Rentang:',
        'sensitivity': 'Sensitivitas:',
        'advantage': 'Keunggulan:',
        'perfect_for': 'Sempurna untuk:',
        
        # Pearson descriptions
        'pearson_purpose': 'Mengukur hubungan linear antara variabel kontinu',
        'pearson_req': 'Mengasumsikan distribusi normal, data interval/rasio, hubungan linear',
        'pearson_when': 'Ketika kedua variabel berdistribusi normal dan hubungannya linear',
        'pearson_formula': 'r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)²Σ(yi - ȳ)²]',
        'pearson_range': '-1 hingga +1 (korelasi negatif sempurna ke positif sempurna)',
        'pearson_sensitivity': 'Sangat sensitif terhadap outlier dan nilai ekstrem',
        
        # Spearman descriptions
        'spearman_purpose': 'Mengukur hubungan monotonik (tidak harus linear)',
        'spearman_req': 'Bekerja dengan data ordinal, interval, atau rasio; non-parametrik',
        'spearman_when': 'Ketika data tidak berdistribusi normal, mengandung outlier, atau melibatkan data ordinal (seperti skala Likert 1-5)',
        'spearman_method': 'Menggunakan perhitungan berbasis peringkat bukan nilai mentah',
        'spearman_advantage': 'Lebih robust terhadap outlier dan distribusi non-normal',
        'spearman_perfect': 'Data survei dengan skala Likert, preferensi peringkat, pengukuran ordinal',
        
        # Table
        'key_diff': 'Perbedaan Utama: Pearson vs Spearman',
        'aspect': 'Aspek',
        'data_type': 'Tipe Data',
        'relationship_type': 'Tipe Hubungan',
        'distribution': 'Distribusi',
        'outliers': 'Outlier',
        'likert_scales': 'Skala Likert (1-5)',
        'calculation': 'Perhitungan',
        'best_app': 'Aplikasi Terbaik',
        
        # Table values
        'continuous': 'Kontinu (interval/rasio)',
        'ordinal_continuous': 'Ordinal atau kontinu',
        'linear_only': 'Hanya linear',
        'monotonic': 'Monotonik (arah yang konsisten)',
        'requires_norm': 'Membutuhkan normalitas',
        'no_assumption': 'Tidak ada asumsi distribusi',
        'highly_sensitive': 'Sangat sensitif',
        'robust_resistant': 'Robust dan resisten',
        'not_recommended': 'Tidak direkomendasikan',
        'ideal_choice': 'Pilihan ideal',
        'uses_raw': 'Menggunakan nilai data mentah',
        'uses_ranked': 'Menggunakan data peringkat',
        'experimental': 'Data eksperimental, pengukuran',
        'survey_research': 'Riset survei, kuesioner',
        
        # When to use
        'when_use_which': 'Kapan Menggunakan Metode Mana?',
        'use_pearson_when': 'Gunakan Pearson ketika:',
        'use_spearman_when': 'Gunakan Spearman ketika:',
        'normal_dist': 'Data berdistribusi normal',
        'linear_rel': 'Hubungan bersifat linear',
        'vars_continuous': 'Variabel bersifat kontinu',
        'no_outliers': 'Tidak ada outlier signifikan',
        'ordinal_data': 'Data bersifat ordinal (skala Likert)',
        'non_normal': 'Distribusi non-normal',
        'presence_outliers': 'Terdapat outlier',
        'monotonic_not_linear': 'Monotonik tapi tidak linear',

           # PDF Report translations (Indonesian)
        'pdf_title': 'LAPORAN ANALISIS STATISTIK',
        'pdf_report_info': 'Informasi Laporan',
        'pdf_generated': 'Dibuat',
        'pdf_total_resp': 'Total Responden',
        'pdf_x_vars': 'Variabel X',
        'pdf_y_vars': 'Variabel Y',
        'pdf_exec_summary': 'RINGKASAN EKSEKUTIF',
        'pdf_exec_text_1': 'Laporan analisis statistik komprehensif ini menyajikan temuan dari data survei dengan',
        'pdf_exec_text_2': 'responden. Analisis mengungkapkan hubungan',
        'pdf_exec_text_3': 'antara variabel X dan Y (koefisien korelasi =',
        'pdf_exec_text_4': 'nilai-p =',
        'pdf_exec_text_5': 'Hubungan tersebut',
        'pdf_statistically_sig': 'signifikan secara statistik',
        'pdf_not_statistically_sig': 'tidak signifikan secara statistik',
        'pdf_exec_text_6': 'pada tingkat α = 0,05. Metode yang dipilih',
        'pdf_exec_text_7': 'dipilih berdasarkan pengujian normalitas distribusi data.',
        'pdf_desc_stats': 'STATISTIK DESKRIPTIF',
        'pdf_variable': 'Variabel:',
        'pdf_statistic': 'Statistik',
        'pdf_value': 'Nilai',
        'pdf_distribution': 'Distribusi:',
        'pdf_normality_test': 'UJI NORMALITAS',
        'pdf_normality_text': 'Uji Shapiro-Wilk dilakukan untuk menilai normalitas distribusi data:',
        'pdf_interpretation_col': 'Interpretasi',
        'pdf_data_follows': 'Data mengikuti distribusi normal',
        'pdf_data_not_follows': 'Data tidak mengikuti distribusi normal',
        'pdf_selected_method': 'Metode Terpilih:',
        'pdf_method_text_1': 'Berdasarkan hasil uji normalitas,',
        'pdf_method_text_2': 'dipilih sebagai metode analisis korelasi yang sesuai.',
        'pdf_pearson_suitable': 'Korelasi Pearson cocok ketika kedua variabel mengikuti distribusi normal.',
        'pdf_spearman_suitable': 'Korelasi Spearman lebih robust untuk distribusi non-normal dan data ordinal.',
        'pdf_corr_analysis': 'ANALISIS KORELASI',
        'pdf_metric': 'Metrik',
        'pdf_interp': 'Interpretasi',
        'pdf_method_used': 'Metode statistik yang digunakan',
        'pdf_relationship': 'hubungan',
        'pdf_sample_size': 'Ukuran Sampel',
        'pdf_num_obs': 'Jumlah pengamatan',
        'pdf_scatter_plot': 'Diagram Sebar dengan Garis Tren:',
        'pdf_trend_line': 'Garis Tren',
        'pdf_interpretation': 'INTERPRETASI',
        'pdf_key_findings': 'Analisis korelasi mengungkapkan temuan utama berikut:',
        'pdf_strength_rel': 'Kekuatan Hubungan:',
        'pdf_strength_text_1': 'Koefisien korelasi r =',
        'pdf_strength_text_2': 'menunjukkan hubungan',
        'pdf_strength_text_3': 'antara variabel. Ini menunjukkan bahwa',
        'pdf_substantial': 'terdapat asosiasi yang substansial',
        'pdf_moderate': 'terdapat asosiasi yang moderat hingga lemah',
        'pdf_between_vars': 'antara variabel X dan Y.',
        'pdf_direction_rel': 'Arah Hubungan:',
        'pdf_direction_text_1': 'Koefisien korelasi',
        'pdf_direction_text_2': 'menunjukkan bahwa ketika X meningkat, Y cenderung',
        'pdf_increase': 'meningkat juga',
        'pdf_decrease': 'menurun',
        'pdf_direction_text_3': 'Hubungan',
        'pdf_direct': 'langsung',
        'pdf_inverse': 'terbalik',
        'pdf_direction_text_4': 'ini',
        'pdf_same_direction': 'menunjukkan kedua variabel bergerak dalam arah yang sama',
        'pdf_opposite_direction': 'menunjukkan variabel bergerak dalam arah berlawanan',
        'pdf_stat_sig': 'Signifikansi Statistik:',
        'pdf_sig_text_1': 'Dengan nilai-p sebesar',
        'pdf_sig_text_2': 'hubungan tersebut',
        'pdf_sig_text_3': 'Ini berarti',
        'pdf_reject_null': 'kita dapat menolak hipotesis nol dan menyimpulkan bahwa korelasi yang diamati tidak mungkin terjadi karena kebetulan',
        'pdf_cannot_reject': 'kita tidak dapat menolak hipotesis nol, dan korelasi yang diamati mungkin disebabkan oleh variasi acak',
        'pdf_important_note': 'Catatan Penting:',
        'pdf_causation': 'Korelasi tidak menyiratkan kausalitas. Meskipun kita mengamati',
        'pdf_sig_association': 'asosiasi yang signifikan',
        'pdf_an_association': 'sebuah asosiasi',
        'pdf_causation_text': 'antara variabel, analisis ini sendiri tidak dapat menentukan apakah satu variabel menyebabkan perubahan pada variabel lainnya.',
        'pdf_conclusion': 'KESIMPULAN',
        'pdf_summary': 'Ringkasan Temuan Utama:',
        'pdf_desc_analysis_sum': 'Analisis Deskriptif:',
        'pdf_desc_text': 'Berhasil menganalisis',
        'pdf_desc_text_2': 'variabel, mengungkapkan pola bermakna dalam distribusi data.',
        'pdf_composite': 'Skor Komposit:',
        'pdf_composite_text': 'Membuat ukuran agregat yang andal (X_total dan Y_total) yang meningkatkan reliabilitas pengukuran dan mengurangi kesalahan acak.',
        'pdf_corr_analysis_sum': 'Analisis Korelasi:',
        'pdf_corr_text_1': 'Menemukan hubungan',
        'pdf_corr_text_2': 'yang',
        'pdf_corr_text_3': 'pada tingkat 0,05.',
        'pdf_method_rigor': 'Ketelitian Metodologis:',
        'pdf_method_text': 'Menerapkan metode statistik yang sesuai',
        'pdf_method_text_2': 'berdasarkan karakteristik distribusi data, memastikan hasil yang valid dan reliabel.',
        'pdf_academic': 'Pelaporan Akademik:',
        'pdf_academic_text': 'Hasil cocok untuk dimasukkan dalam makalah akademik, tesis, dan laporan penelitian dengan kutipan metode dan keterbatasan yang tepat.',
        'pdf_recommendations': 'Rekomendasi:',
        'pdf_rec_1': 'Pertimbangkan untuk melakukan analisis tambahan untuk mengeksplorasi variabel perancu potensial',
        'pdf_rec_2': 'Periksa perbedaan subkelompok jika berlaku untuk konteks penelitian Anda',
        'pdf_rec_3': 'Replikasi temuan dengan sampel independen untuk memvalidasi hasil',
        'pdf_rec_4': 'Pertimbangkan metode kualitatif untuk memahami mekanisme di balik hubungan yang diamati',
        'pdf_footer': 'Laporan dibuat oleh Data Analytics Platform | © 2024 | Dibuat pada',
        'pdf_download_btn': 'Unduh Laporan Analisis Lengkap dengan Grafik (PDF)',
        'pdf_success': 'Laporan PDF dengan semua grafik berhasil dibuat!',
        'pdf_includes': 'Laporan ini mencakup: Ringkasan Eksekutif, Statistik Deskriptif dengan Grafik, Uji Normalitas, Analisis Korelasi dengan Diagram Sebar, Interpretasi Terperinci, dan Kesimpulan.', 
    }
}

def t(key):
    """Get translation for current language"""
    return translations[st.session_state.language].get(key, key)

# Custom CSS for styling
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 8px;
        color: #1976d2;
        font-size: 18px;
        font-weight: 700;
        padding: 10px 30px;
        border: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: 2px solid white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(102, 126, 234, 0.3);
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 28px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
</style>
""", unsafe_allow_html=True)

# Language selector in sidebar
with st.sidebar:
    st.markdown("### 🌐 Language / Bahasa")
    language = st.radio("", ["English", "Bahasa Indonesia"], index=0 if st.session_state.language == 'en' else 1, label_visibility="collapsed")
    if language == "English":
        st.session_state.language = 'en'
    else:
        st.session_state.language = 'id'

# Helper Functions
def descriptive_numeric(series):
    series = series.dropna()
    return {
        t('count'): len(series),
        t('mean'): series.mean(),
        t('median'): series.median(),
        t('std_dev'): series.std(),
        t('variance'): series.var(),
        t('min'): series.min(),
        t('max'): series.max()
    }

def freq_table(series):
    vc = series.value_counts(dropna=False)
    pct = (vc / len(series) * 100).round(2)
    return pd.DataFrame({
        t('category'): vc.index.astype(str),
        t('frequency'): vc.values,
        t('percentage'): pct.values
    })

def corr_strength(r):
    r = abs(r)
    if r < 0.2: return "Very Weak"
    if r < 0.4: return "Weak"
    if r < 0.6: return "Moderate"
    if r < 0.8: return "Strong"
    return "Very Strong"

def is_likert(series):
    vals = series.dropna().unique()
    return all(v in [1,2,3,4,5] for v in vals)

# Create tabs
tab1, tab2, tab3 = st.tabs([f"🏠  {t('title').upper()[:4]}", "📘  INTRODUCTION", "📊  ANALYSIS"])

# ==================== TAB 1: HOME PAGE ====================
with tab1:
    st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .quote-card {
            background: rgba(255, 255, 255, 0.1);
            border-left: 4px solid #FFD700;
            padding: 15px;
            border-radius: 10px;
            font-style: italic;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="text-align: center; padding: 20px;">', unsafe_allow_html=True)
    st.markdown(f'<h1 style="color: white; font-size: 3rem; margin-bottom: 10px;">📊 {t("title")}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: white; font-size: 1.3rem;">{t("subtitle")}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    QUOTES = [
        "Without data, you're just another person with an opinion. - W. Edwards Deming",
        "Data is a precious thing and will last longer than the systems themselves. - Tim Berners-Lee",
        "The goal is to turn data into information, and information into insight. - Carly Fiorina",
        "In God we trust. All others must bring data. - W. Edwards Deming",
        "Data really powers everything that we do. - Jeff Weiner"
    ]
    
    quote = random.choice(QUOTES)
    st.markdown(f"""
    <div class="quote-card">
        <p style="color: white; margin: 0; font-size: 1.1rem;">"{quote.split(' - ')[0]}"</p>
        <p style="color: rgba(255, 255, 255, 0.7); text-align: right; margin: 5px 0 0 0; font-size: 1rem;">
        — {quote.split(' - ')[1]}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="glass-card">
        <h3 style="color: white; margin-bottom: 10px;">🌟 {t('welcome')}</h3>
        <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.05rem;">
        {t('welcome_text')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<h3 style="color: white; margin: 30px 0 15px 0;">✨ {t("core_features")}</h3>', unsafe_allow_html=True)
    
    features = [
        ("📋", t('descriptive_stats'), t('descriptive_desc')),
        ("🔗", t('spearman'), t('spearman_desc')),
        ("📊", t('data_viz'), t('data_viz_desc')),
        ("📈", t('regression'), t('regression_desc')),
        ("🎯", t('stat_testing'), t('stat_testing_desc')),
        ("📊", t('corr_matrix'), t('corr_matrix_desc'))
    ]
    
    cols = st.columns(3)
    for idx, (icon, title, desc) in enumerate(features):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="glass-card">
                <div style="font-size: 1.8rem; margin-bottom: 8px;">{icon}</div>
                <h4 style="color: white; margin: 0 0 5px 0;">{title}</h4>
                <p style="color: rgba(255, 255, 255, 0.8); font-size: 0.9rem; margin: 0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; color: rgba(255, 255, 255, 0.6); padding: 20px 0;">
        <p style="font-size: 1rem;">{t('footer')}</p>
        <p style="font-size: 0.9rem;">{t('footer_sub')}</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 2: INTRODUCTION ====================
with tab2:
    st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
        }
        
        .tech-card-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; padding: 2.5rem 1.5rem; text-align: center; transition: all 0.4s ease; border: 3px solid white; height: 180px; box-shadow: 0 8px 20px rgba(102, 126, 234, 0.5); display: flex; flex-direction: column; justify-content: center; }
        .tech-card-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 20px; padding: 2.5rem 1.5rem; text-align: center; transition: all 0.4s ease; border: 3px solid white; height: 180px; box-shadow: 0 8px 20px rgba(240, 147, 251, 0.5); display: flex; flex-direction: column; justify-content: center; }
        .tech-card-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 20px; padding: 2.5rem 1.5rem; text-align: center; transition: all 0.4s ease; border: 3px solid white; height: 180px; box-shadow: 0 8px 20px rgba(79, 172, 254, 0.5); display: flex; flex-direction: column; justify-content: center; }
        .tech-card-4 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); border-radius: 20px; padding: 2.5rem 1.5rem; text-align: center; transition: all 0.4s ease; border: 3px solid white; height: 180px; box-shadow: 0 8px 20px rgba(67, 233, 123, 0.5); display: flex; flex-direction: column; justify-content: center; }
        .tech-card-5 { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); border-radius: 20px; padding: 2.5rem 1.5rem; text-align: center; transition: all 0.4s ease; border: 3px solid white; height: 180px; box-shadow: 0 8px 20px rgba(250, 112, 154, 0.5); display: flex; flex-direction: column; justify-content: center; }
        .tech-card-6 { background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); border-radius: 20px; padding: 2.5rem 1.5rem; text-align: center; transition: all 0.4s ease; border: 3px solid white; height: 180px; box-shadow: 0 8px 20px rgba(48, 207, 208, 0.5); display: flex; flex-direction: column; justify-content: center; }
        
        .tech-card-1:hover, .tech-card-2:hover, .tech-card-3:hover,
        .tech-card-4:hover, .tech-card-5:hover, .tech-card-6:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
        }
        
        .tech-icon { font-size: 3.5rem; margin-bottom: 0.5rem; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3)); }
        .tech-name { color: white; font-size: 1.4rem; font-weight: 700; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); margin: 0; }
        .about-section { background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px; margin: 2rem 0; box-shadow: 0 8px 20px rgba(0,0,0,0.2); }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem 0 2rem 0;">
        <h1 style="margin-bottom: 0.5rem; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">📊 {t('platform_title')}</h1>
        <p style="font-size: 1.3rem; color: white; margin-bottom: 1rem; font-weight: 600; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{t('platform_subtitle')}</p>
        <div style="padding: 1.2rem; background: rgba(255, 255, 255, 0.2); border-radius: 12px; display: inline-block; margin: 1rem auto; border-left: 5px solid #FFD700; box-shadow: 0 4px 12px rgba(0,0,0,0.2); backdrop-filter: blur(10px);">
            <p style="font-style: italic; color: white; margin: 0; font-size: 1.15rem; font-weight: 600; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">"It is a capital mistake to theorize before one has data." — Sherlock Holmes</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 3px; background: linear-gradient(90deg, #FFD700, #FFA500, #FFD700); margin: 3rem 0; border-radius: 3px;"></div>', unsafe_allow_html=True)
    
    st.markdown(f'<h2 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🎯 {t("objectives")}</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.15); padding: 1.8rem; border-radius: 15px; height: 100%; box-shadow: 0 4px 12px rgba(0,0,0,0.2); backdrop-filter: blur(10px); border: 2px solid rgba(255,255,255,0.3);">
            <h3 style="color: white; font-weight: 700; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🌍 {t('global_access')}</h3>
            <ul style="color: white; line-height: 1.9; font-size: 1.05rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                <li><strong>{t('global_text_1')}</strong></li>
                <li><strong>{t('global_text_2')}</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.15); padding: 1.8rem; border-radius: 15px; height: 100%; box-shadow: 0 4px 12px rgba(0,0,0,0.2); backdrop-filter: blur(10px); border: 2px solid rgba(255,255,255,0.3);">
            <h3 style="color: white; font-weight: 700; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">📈 {t('comprehensive')}</h3>
            <ul style="color: white; line-height: 1.9; font-size: 1.05rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                <li><strong>{t('comp_text_1')}</strong></li>
                <li><strong>{t('comp_text_2')}</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 3px; background: linear-gradient(90deg, #FFD700, #FFA500, #FFD700); margin: 3rem 0; border-radius: 3px;"></div>', unsafe_allow_html=True)
    
    st.markdown(f'<h2 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🛠️ {t("tech_stack")}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: white; font-size: 1.08rem; margin-bottom: 2rem; font-weight: 500; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{t("tech_text")}</p>', unsafe_allow_html=True)
    
    tech_stack = [
        {"icon": "🐍", "name": "Python 3.11+", "class": "tech-card-1"},
        {"icon": "🐼", "name": "Pandas", "class": "tech-card-2"},
        {"icon": "📊", "name": "Plotly", "class": "tech-card-3"},
        {"icon": "⚡", "name": "Streamlit", "class": "tech-card-4"},
        {"icon": "🔢", "name": "NumPy", "class": "tech-card-5"},
        {"icon": "🔬", "name": "SciPy", "class": "tech-card-6"},
    ]
    
    cols = st.columns(3)
    for idx, tech in enumerate(tech_stack):
        with cols[idx % 3]:
            st.markdown(f'<div class="{tech["class"]}"><div class="tech-icon">{tech["icon"]}</div><h3 class="tech-name">{tech["name"]}</h3></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="height: 3px; background: linear-gradient(90deg, #FFD700, #FFA500, #FFD700); margin: 3rem 0; border-radius: 3px;"></div>', unsafe_allow_html=True)
    
    st.markdown(f'<h2 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">👥 {t("our_team")}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: white; font-size: 1.08rem; margin-bottom: 2rem; font-weight: 500; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{t("team_text")}</p>', unsafe_allow_html=True)
    
    team_members = [
        {"name": "Hevita Zhofany Putri", "role": "Data Analyst", "id": "004202400016", "icon": "📈", "color": "#4CAF50"},
        {"name": "Ristia Angelina Purba", "role": "Data Scientist", "id": "004202400071", "icon": "👩‍🔬", "color": "#2196F3"},
        {"name": "Mika Lusia Panjaitan", "role": "Statistical Systems Developer", "id": "004202400101", "icon": "👩‍💻", "color": "#FF9800"},
        {"name": "Sarah Aulya Fitri Ritonga", "role": "Project Manager", "id": "004202400090", "icon": "👩‍💼", "color": "#9C27B0"}
    ]
    
    cols = st.columns(2)
    for idx, member in enumerate(team_members):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.15); border-radius: 15px; padding: 2rem; margin: 1.5rem 0; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2); border-top: 5px solid {member['color']}; backdrop-filter: blur(10px);">
                <div style="display: flex; align-items: center; gap: 1.5rem;">
                    <div style="width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.2rem; color: white; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3); background: linear-gradient(135deg, {member['color']}, {member['color']}dd);">{member['icon']}</div>
                    <div style="flex: 1;">
                        <div style="font-size: 1.4rem; font-weight: 700; color: white; margin-bottom: 0.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{member['name']}</div>
                        <div style="font-size: 1.1rem; font-weight: 600; color: white; margin-bottom: 0.5rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{member['role']}</div>
                        <div style="color: rgba(255,255,255,0.9); font-size: 0.95rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">Student ID: {member['id']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 3px; background: linear-gradient(90deg, #FFD700, #FFA500, #FFD700); margin: 3rem 0; border-radius: 3px;"></div>', unsafe_allow_html=True)
    
# About the Analysis - COMPLETELY FIXED VERSION
    st.markdown(f'<h2 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); margin-bottom: 1.5rem;">📊 {t("about_analysis")}</h2>', unsafe_allow_html=True)
    
    # Block 1: Introduction
    st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.markdown(f'<h3 style="color: white; background: linear-gradient(135deg, #1e88e5, #1565c0); padding: 1rem; border-radius: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); margin: -2rem -2rem 1.5rem -2rem;">{t("about_text")}</h3>', unsafe_allow_html=True)
    
    st.markdown(f'<ol style="color: #333; font-size: 1.05rem; line-height: 1.8; margin-top: 1rem;"><li><strong style="color: #333;">{t("descriptive_analysis")}</strong></li><li><strong style="color: #333;">{t("association_analysis")}</strong></li></ol>', unsafe_allow_html=True)
    
    # Descriptive Analysis Section
    st.markdown(f'<h3 style="color: #333; margin-top: 2rem; border-bottom: 3px solid #1565c0; padding-bottom: 0.5rem;">{t("desc_analysis_title")}</h3>', unsafe_allow_html=True)
    st.markdown(f'<ul style="color: #333; font-size: 1.05rem; line-height: 1.8;"><li><strong style="color: #333;">{t("basic_stats_title")}</strong> {t("basic_stats_text")}</li><li><strong style="color: #333;">{t("distribution_title")}</strong> {t("distribution_text")}</li><li><strong style="color: #333;">{t("summaries_title")}</strong> {t("summaries_text")}</li></ul>', unsafe_allow_html=True)
    
    # Association Analysis Section
    st.markdown(f'<h3 style="color: #333; margin-top: 2rem; border-bottom: 3px solid #1565c0; padding-bottom: 0.5rem;">{t("assoc_analysis_title")}</h3>', unsafe_allow_html=True)
    st.markdown(f'<ul style="color: #333; font-size: 1.05rem; line-height: 1.8;"><li><strong style="color: #333;">{t("spearman_coef")}</strong></li><li><strong style="color: #333;">{t("p_value")}</strong></li><li><strong style="color: #333;">{t("visualizations")}</strong></li><li><strong style="color: #333;">{t("interpretations")}</strong></li></ul>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Correlation Methods Section
    st.markdown(f'<div class="about-section"><h3 style="color: #1565c0; margin-top: 2rem; border-bottom: 3px solid #1565c0; padding-bottom: 0.5rem;">📈 {t("understanding_corr")}</h3></div>', unsafe_allow_html=True)
    
    # Pearson Card
    pearson_html = f'''<div class="about-section"><div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1565c0; margin: 1.5rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <h4 style="color: #0d47a1; margin-top: 0; font-size: 1.3rem;">📊 {t("pearson_corr")}</h4>
    <ul style="color: #333; line-height: 1.8; margin: 0;">
    <li><strong>{t("purpose")}</strong> {t("pearson_purpose")}</li>
    <li><strong>{t("requirements")}</strong> {t("pearson_req")}</li>
    <li><strong>{t("when_use")}</strong> {t("pearson_when")}</li>
    <li><strong>{t("formula")}</strong> {t("pearson_formula")}</li>
    <li><strong>{t("range_val")}</strong> {t("pearson_range")}</li>
    <li><strong>{t("sensitivity")}</strong> {t("pearson_sensitivity")}</li>
    </ul></div></div>'''
    st.markdown(pearson_html, unsafe_allow_html=True)
    
    # Spearman Card
    spearman_html = f'''<div class="about-section"><div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff9800; margin: 1.5rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <h4 style="color: #e65100; margin-top: 0; font-size: 1.3rem;">📈 {t("spearman_corr")}</h4>
    <ul style="color: #333; line-height: 1.8; margin: 0;">
    <li><strong>{t("purpose")}</strong> {t("spearman_purpose")}</li>
    <li><strong>{t("requirements")}</strong> {t("spearman_req")}</li>
    <li><strong>{t("when_use")}</strong> {t("spearman_when")}</li>
    <li><strong>{t("method_calc")}</strong> {t("spearman_method")}</li>
    <li><strong>{t("advantage")}</strong> {t("spearman_advantage")}</li>
    <li><strong>{t("perfect_for")}</strong> {t("spearman_perfect")}</li>
    </ul></div></div>'''
    st.markdown(spearman_html, unsafe_allow_html=True)
    
    # Comparison Table
    comparison_table = f'''
    <div class="about-section">
        <div style="background: linear-gradient(135deg, #f1f8e9 0%, #dcedc8 100%); padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h4 style="color: #33691e; margin-top: 0; font-size: 1.3rem;">🔍 {t("key_diff")}</h4>
            <table style="width: 100%; border-collapse: collapse; color: #333; margin-top: 1rem;">
                <thead>
                    <tr style="background: linear-gradient(135deg, #aed581, #9ccc65);">
                        <th style="padding: 12px; text-align: left; border: 1px solid #689f38; color: #1b5e20; font-weight: 700;">{t("aspect")}</th>
                        <th style="padding: 12px; text-align: left; border: 1px solid #689f38; color: #1b5e20; font-weight: 700;">Pearson</th>
                        <th style="padding: 12px; text-align: left; border: 1px solid #689f38; color: #1b5e20; font-weight: 700;">Spearman</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background: #ffffff;">
                        <td style="padding: 10px; border: 1px solid #c5e1a5;"><strong>{t("data_type")}</strong></td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("continuous")}</td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("ordinal_continuous")}</td>
                    </tr>
                    <tr style="background: #f9fbe7;">
                        <td style="padding: 10px; border: 1px solid #c5e1a5;"><strong>{t("relationship_type")}</strong></td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("linear_only")}</td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("monotonic")}</td>
                    </tr>
                    <tr style="background: #ffffff;">
                        <td style="padding: 10px; border: 1px solid #c5e1a5;"><strong>{t("distribution")}</strong></td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("requires_norm")}</td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("no_assumption")}</td>
                    </tr>
                    <tr style="background: #f9fbe7;">
                        <td style="padding: 10px; border: 1px solid #c5e1a5;"><strong>{t("outliers")}</strong></td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">❌ {t("highly_sensitive")}</td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">✅ {t("robust_resistant")}</td>
                    </tr>
                    <tr style="background: #ffffff;">
                        <td style="padding: 10px; border: 1px solid #c5e1a5;"><strong>{t("likert_scales")}</strong></td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">❌ {t("not_recommended")}</td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">✅ {t("ideal_choice")}</td>
                    </tr>
                    <tr style="background: #f9fbe7;">
                        <td style="padding: 10px; border: 1px solid #c5e1a5;"><strong>{t("calculation")}</strong></td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("uses_raw")}</td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("uses_ranked")}</td>
                    </tr>
                    <tr style="background: #ffffff;">
                        <td style="padding: 10px; border: 1px solid #c5e1a5;"><strong>{t("best_app")}</strong></td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("experimental")}</td>
                        <td style="padding: 10px; border: 1px solid #c5e1a5;">{t("survey_research")}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    '''
    st.markdown(comparison_table, unsafe_allow_html=True)
    
    # When to Use
    when_to_use = f'''
    <div class="about-section">
        <div style="background: linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%); padding: 1.5rem; border-radius: 10px; border-left: 5px solid #0288d1; margin: 1.5rem 0;">
            <h4 style="color: #01579b; margin-top: 0;">💡 {t("when_use_which")}</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                <div style="background: white; padding: 1rem; border-radius: 8px; border: 2px solid #4fc3f7;">
                    <h5 style="color: #0277bd; margin-top: 0;">{t("use_pearson_when")}</h5>
                    <ul style="color: #333; font-size: 0.95rem; line-height: 1.6; margin: 0;">
                        <li>{t("normal_dist")}</li>
                        <li>{t("linear_rel")}</li>
                        <li>{t("vars_continuous")}</li>
                        <li>{t("no_outliers")}</li>
                    </ul>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 8px; border: 2px solid #ffb74d;">
                    <h5 style="color: #e65100; margin-top: 0;">{t("use_spearman_when")}</h5>
                    <ul style="color: #333; font-size: 0.95rem; line-height: 1.6; margin: 0;">
                        <li>{t("ordinal_data")}</li>
                        <li>{t("non_normal")}</li>
                        <li>{t("presence_outliers")}</li>
                        <li>{t("monotonic_not_linear")}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    '''
    st.markdown(when_to_use, unsafe_allow_html=True)
    
    # Program Objectives
    st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.markdown(f'<h3 style="color: #1565c0; margin-top: 2rem; border-bottom: 3px solid #1565c0; padding-bottom: 0.5rem;">🎯 {t("program_obj")}</h3>', unsafe_allow_html=True)
    st.markdown(f'<ol style="color: #333; font-size: 1.05rem; line-height: 1.8;"><li>{t("obj_1")}</li><li>{t("obj_2")}</li><li>{t("obj_3")}</li><li>{t("obj_4")}</li><li>{t("obj_5")}</li></ol>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 3: ANALYSIS ====================
with tab3:
    st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #0d47a1, #1976d2, #42a5f5); }
        .content-box { background: white; padding: 28px; border-radius: 18px; margin-bottom: 28px; box-shadow: 0 12px 35px rgba(0,0,0,0.15); }
        .stats-card { background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%); border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-left: 5px solid #1e88e5; transition: all 0.3s ease; }
        .stats-card:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(0,0,0,0.12); }
        .interpretation-box { background: linear-gradient(135deg, #e3f2fd 0%, #f4f8ff 100%); border-left: 6px solid #1e88e5; padding: 1.5rem; border-radius: 12px; margin-top: 1.5rem; color: #1565c0; font-size: 15px; box-shadow: 0 4px 12px rgba(30, 136, 229, 0.1); }
        .metric-badge { display: inline-block; background: linear-gradient(135deg, #1e88e5, #1565c0); color: white; padding: 8px 16px; border-radius: 20px; font-weight: 600; font-size: 14px; margin: 5px; box-shadow: 0 3px 8px rgba(30, 136, 229, 0.3); }
        h1 { text-align: center; color: white; font-weight: 800; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); }
        h2 { color: #0d47a1; font-weight: 700; margin-top: 1rem; }
        h3 { color: #1565c0; font-weight: 700; margin-top: 1rem; }
        .stDataFrame { border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
    </style>
    """, unsafe_allow_html=True)
    
    sns.set_theme(style="whitegrid", palette=["#1e88e5", "#42a5f5", "#90caf9"])
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = '#f8f9ff'
    
    st.markdown("<h1>📊 STATISTICAL ANALYZER PRO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:white;font-size:18px;text-shadow: 1px 1px 2px rgba(0,0,0,0.3);'>Advanced Descriptive & Association Analysis</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown(f"## 📤 {t('upload_dataset')}")
    uploaded_file = st.file_uploader(t('accepted_formats'), type=["csv", "xlsx", "xls"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        st.success(f"✅ {t('dataset_loaded')}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"<div class='metric-badge'>📊 {t('rows')}: {len(df)}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='metric-badge'>📋 {t('columns')}: {len(df.columns)}</div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div class='metric-badge'>💾 {t('size')}: {df.memory_usage(deep=True).sum() / 1024:.1f} KB</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.dataframe(df.head(), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        st.markdown(f"## 🔍 {t('variable_selection')}")
        col1, col2 = st.columns(2)
        with col1:
            x_items = st.multiselect(f"📊 {t('select_x')}", df.columns, key="x_vars")
        with col2:
            y_items = st.multiselect(f"📈 {t('select_y')}", df.columns, key="y_vars")
        create_total = st.checkbox(f"✨ {t('create_composite')}", value=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button(f"▶️ {t('run_analysis')}", type="primary", use_container_width=True):
            data = df.copy()

            if create_total:
                if x_items:
                    data["X_total"] = data[x_items].apply(pd.to_numeric, errors="coerce").sum(axis=1)
                if y_items:
                    data["Y_total"] = data[y_items].apply(pd.to_numeric, errors="coerce").sum(axis=1)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"## 📊 {t('desc_analysis')}")
            
            variables_to_analyze = []
            if x_items:
                variables_to_analyze.extend(x_items)
            if y_items:
                variables_to_analyze.extend(y_items)
            if create_total:
                if "X_total" in data.columns:
                    variables_to_analyze.append("X_total")
                if "Y_total" in data.columns:
                    variables_to_analyze.append("Y_total")
            
            for col in variables_to_analyze:
                if col not in data.columns:
                    continue

                st.markdown("<div class='content-box'>", unsafe_allow_html=True)
                st.markdown(f"### 📌 {t('variable')}: {col}")
                series = data[col]

                if pd.api.types.is_numeric_dtype(series):
                    desc = descriptive_numeric(series)
                    
                    st.markdown("<div class='stats-card'>", unsafe_allow_html=True)
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric(f"📊 {list(desc.keys())[0]}", f"{list(desc.values())[0]}")
                        st.metric(f"📈 {list(desc.keys())[1]}", f"{list(desc.values())[1]:.2f}")
                    with col2:
                        st.metric(f"🎯 {list(desc.keys())[2]}", f"{list(desc.values())[2]:.2f}")
                        st.metric(f"📉 {list(desc.keys())[5]}", f"{list(desc.values())[5]:.2f}")
                    with col3:
                        st.metric(f"📊 {list(desc.keys())[3]}", f"{list(desc.values())[3]:.2f}")
                        st.metric(f"📈 {list(desc.keys())[6]}", f"{list(desc.values())[6]:.2f}")
                    with col4:
                        st.metric(f"🔄 {list(desc.keys())[4]}", f"{list(desc.values())[4]:.2f}")
                        st.metric(f"📏 {t('range')}", f"{list(desc.values())[6] - list(desc.values())[5]:.2f}")
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)

                    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
                    
                    clean_data = series.dropna()
                    ax[0].hist(clean_data, bins=20, alpha=0.7, color='#1e88e5', edgecolor='white', linewidth=1.2)
                    ax[0].axvline(list(desc.values())[1], color='#d32f2f', linestyle='--', linewidth=2, label=f'{list(desc.keys())[1]}: {list(desc.values())[1]:.2f}')
                    ax[0].axvline(list(desc.values())[2], color='#388e3c', linestyle='--', linewidth=2, label=f'{list(desc.keys())[2]}: {list(desc.values())[2]:.2f}')
                    ax[0].set_title(f'Distribution of {col}', fontsize=14, fontweight='bold', pad=15)
                    ax[0].set_xlabel(col, fontsize=12, fontweight='bold')
                    ax[0].set_ylabel(t('frequency'), fontsize=12, fontweight='bold')
                    ax[0].legend(loc='upper right', framealpha=0.9)
                    ax[0].grid(True, alpha=0.3, linestyle='--')
                    ax[0].spines['top'].set_visible(False)
                    ax[0].spines['right'].set_visible(False)
                    
                    bp = ax[1].boxplot(clean_data, vert=False, patch_artist=True,
                                      boxprops=dict(facecolor='#90caf9', edgecolor='#1565c0', linewidth=2),
                                      whiskerprops=dict(color='#1565c0', linewidth=2),
                                      capprops=dict(color='#1565c0', linewidth=2),
                                      medianprops=dict(color='#d32f2f', linewidth=3),
                                      flierprops=dict(marker='o', markerfacecolor='#ff6b6b', markersize=8, markeredgecolor='white'))
                    ax[1].set_title(f'Boxplot of {col}', fontsize=14, fontweight='bold', pad=15)
                    ax[1].set_xlabel(col, fontsize=12, fontweight='bold')
                    ax[1].grid(True, alpha=0.3, linestyle='--', axis='x')
                    ax[1].spines['top'].set_visible(False)
                    ax[1].spines['right'].set_visible(False)
                    ax[1].spines['left'].set_visible(False)
                    
                    plt.tight_layout()
                    st.pyplot(fig)
                    plt.close(fig)

                    st.markdown(f"""
                    <div class="interpretation-box">
                    <h4 style="color: #1565c0; margin-top: 0;">🔍 {t('key_insights')}</h4>
                    <ul style="margin: 0; padding-left: 1.5rem; line-height: 1.8;">
                        <li><strong>{t('central_tendency')}:</strong> {list(desc.keys())[1]} = {list(desc.values())[1]:.2f}, {list(desc.keys())[2]} = {list(desc.values())[2]:.2f}</li>
                        <li><strong>{t('spread')}:</strong> {list(desc.keys())[3]} = {list(desc.values())[3]:.2f}</li>
                        <li><strong>{t('range')}:</strong> {list(desc.values())[5]:.2f} to {list(desc.values())[6]:.2f}</li>
                    </ul>
                    </div>
                    """, unsafe_allow_html=True)

                    if is_likert(series):
                        st.markdown(f"""
                        <div class="interpretation-box" style="border-left-color: #9c27b0; background: linear-gradient(135deg, #f3e5f5 0%, #fce4ec 100%);">
                        <h4 style="color: #7b1fa2; margin-top: 0;">🎯 {t('likert_detected')}</h4>
                        <p style="margin: 0;">{t('likert_text')}</p>
                        </div>
                        """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"#### 📊 {t('frequency_dist')}")
                freq = freq_table(series)
                
                st.dataframe(freq.style.background_gradient(subset=[t('frequency')], cmap='Blues').format({t('percentage'): '{:.2f}%'}), use_container_width=True)
                
                fig_freq, ax_freq = plt.subplots(figsize=(10, 4))
                colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(freq)))
                bars = ax_freq.bar(range(len(freq)), freq[t('frequency')], color=colors, edgecolor='white', linewidth=1.5)
                ax_freq.set_xticks(range(len(freq)))
                ax_freq.set_xticklabels(freq[t('category')], rotation=45, ha='right')
                ax_freq.set_title(f'{t("frequency_dist")}: {col}', fontsize=14, fontweight='bold', pad=15)
                ax_freq.set_xlabel(t('category'), fontsize=12, fontweight='bold')
                ax_freq.set_ylabel(t('frequency'), fontsize=12, fontweight='bold')
                ax_freq.grid(True, alpha=0.3, linestyle='--', axis='y')
                ax_freq.spines['top'].set_visible(False)
                ax_freq.spines['right'].set_visible(False)
                
                for i, bar in enumerate(bars):
                    height = bar.get_height()
                    ax_freq.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}\n({freq[t("percentage")].iloc[i]:.1f}%)', ha='center', va='bottom', fontsize=9, fontweight='bold')
                
                plt.tight_layout()
                st.pyplot(fig_freq)
                plt.close(fig_freq)

                st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<div class='content-box'>", unsafe_allow_html=True)
            st.markdown(f"## 🧪 {t('normality_test')}")
            
            x_norm = stats.shapiro(data["X_total"].dropna()).pvalue if "X_total" in data else 0
            y_norm = stats.shapiro(data["Y_total"].dropna()).pvalue if "Y_total" in data else 0

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="stats-card" style="border-left-color: {'#4caf50' if x_norm > 0.05 else '#f44336'};">
                    <h4 style="color: #1565c0; margin-top: 0;">X_total</h4>
                    <p style="font-size: 1.8rem; font-weight: bold; color: {'#4caf50' if x_norm > 0.05 else '#f44336'}; margin: 0.5rem 0;">p = {x_norm:.4f}</p>
                    <p style="margin: 0; color: #666;">{'✅ ' + t('normal') if x_norm > 0.05 else '❌ ' + t('non_normal')}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="stats-card" style="border-left-color: {'#4caf50' if y_norm > 0.05 else '#f44336'};">
                    <h4 style="color: #1565c0; margin-top: 0;">Y_total</h4>
                    <p style="font-size: 1.8rem; font-weight: bold; color: {'#4caf50' if y_norm > 0.05 else '#f44336'}; margin: 0.5rem 0;">p = {y_norm:.4f}</p>
                    <p style="margin: 0; color: #666;">{'✅ ' + t('normal') if y_norm > 0.05 else '❌ ' + t('non_normal')}</p>
                </div>
                """, unsafe_allow_html=True)

            method_name = t('pearson') if (x_norm > 0.05 and y_norm > 0.05) else t('spearman_rank')
            st.markdown(f"""
            <div class="interpretation-box">
            <p style="margin: 0; padding: 1rem; background: rgba(30, 136, 229, 0.1); border-radius: 8px; font-weight: 600;">📊 <strong>{t('method')}: {method_name}</strong></p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<div class='content-box'>", unsafe_allow_html=True)
            st.markdown(f"## 🔗 {t('association')}")

            if x_norm > 0.05 and y_norm > 0.05:
                r, p = stats.pearsonr(data["X_total"], data["Y_total"])
                method = t('pearson')
            else:
                r, p = stats.spearmanr(data["X_total"], data["Y_total"])
                method = t('spearman_rank')

            strength = corr_strength(r)
            direction = t('positive') if r > 0 else t('negative')

            st.markdown(f"""
            <div class="stats-card" style="border-left-color: #9c27b0;">
                <h4 style="color: #7b1fa2; margin-top: 0;">📐 {method}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)

            fig, ax = plt.subplots(figsize=(10, 7))
            
            scatter = ax.scatter(data["X_total"], data["Y_total"], c=data["Y_total"], cmap='viridis', alpha=0.6, s=100, edgecolors='white', linewidth=1.5)
            
            z = np.polyfit(data["X_total"].dropna(), data["Y_total"].dropna(), 1)
            p_fit = np.poly1d(z)
            x_line = np.linspace(data["X_total"].min(), data["X_total"].max(), 100)
            ax.plot(x_line, p_fit(x_line), "r--", linewidth=3, alpha=0.8, label='Trend')
            
            ax.set_xlabel("X_total", fontsize=14, fontweight='bold')
            ax.set_ylabel("Y_total", fontsize=14, fontweight='bold')
            ax.set_title(f'{method}\nr = {r:.3f}, p = {p:.4f}', fontsize=16, fontweight='bold', pad=20)
            ax.legend(fontsize=12)
            ax.grid(True, alpha=0.3)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            cbar = plt.colorbar(scatter, ax=ax)
            cbar.set_label('Y_total', fontsize=12, fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)

            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class="stats-card" style="text-align: center;">
                    <h5 style="color: #666; margin: 0;">{t('coefficient')}</h5>
                    <p style="font-size: 2rem; font-weight: bold; color: #1e88e5; margin: 0.5rem 0;">{r:.3f}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="stats-card" style="text-align: center;">
                    <h5 style="color: #666; margin: 0;">{t('strength')}</h5>
                    <p style="font-size: 1.3rem; font-weight: bold; color: #7b1fa2; margin: 0.5rem 0;">{strength}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="stats-card" style="text-align: center;">
                    <h5 style="color: #666; margin: 0;">{t('direction')}</h5>
                    <p style="font-size: 1.3rem; font-weight: bold; color: {'#4caf50' if r > 0 else '#f44336'}; margin: 0.5rem 0;">{direction}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                sig_text = t('yes') if p < 0.05 else t('no')
                st.markdown(f"""
                <div class="stats-card" style="text-align: center;">
                    <h5 style="color: #666; margin: 0;">{t('significance')}</h5>
                    <p style="font-size: 1.3rem; font-weight: bold; color: {'#4caf50' if p < 0.05 else '#f44336'}; margin: 0.5rem 0;">{sig_text}</p>
                    <p style="font-size: 0.9rem; color: #666; margin: 0;">p = {p:.4f}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="interpretation-box">
            <h4 style="color: #1565c0; margin-top: 0;">🎯 {t('interpretation')}</h4>
            <ul style="margin: 0; padding-left: 1.5rem; line-height: 1.8;">
                <li>r = {r:.3f} → <strong>{strength.lower()}</strong> {t('relationship')}</li>
                <li><strong>{direction}</strong> {t('correlation')}</li>
                <li>p = {p:.4f} → {'<strong>' + t('significant') + '</strong>' if p < 0.05 else '<strong>' + t('not_significant') + '</strong>'}</li>
                <li><strong>{t('note')}:</strong> {t('causation_note')}</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="content-box">
            <h2 style="color: #1565c0;">🎓 {t('conclusion')}</h2>
            <div class="stats-card" style="border-left-color: #4caf50;">
                <h4 style="color: #2e7d32; margin-top: 0;">✅ {t('key_findings')}</h4>
                <ul style="margin: 0; padding-left: 1.5rem; line-height: 1.8; color: #333;">
                    <li>{t('finding_1')}</li>
                    <li>{t('finding_2')}</li>
                    <li>{t('finding_3')}</li>
                    <li>{t('finding_4')}</li>
                </ul>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            # PDF GENERATION WITH CHARTS - MULTILINGUAL (FIXED FOR CLOUD)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='content-box'>", unsafe_allow_html=True)
st.markdown("## 📄 Download Report")

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    from io import BytesIO
    
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=30)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor('#0d47a1'), spaceAfter=30, alignment=TA_CENTER, fontName='Helvetica-Bold')
    heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=16, textColor=colors.HexColor('#1565c0'), spaceAfter=12, spaceBefore=12, fontName='Helvetica-Bold')
    subheading_style = ParagraphStyle('CustomSubHeading', parent=styles['Heading3'], fontSize=14, textColor=colors.HexColor('#1976d2'), spaceAfter=10, spaceBefore=10, fontName='Helvetica-Bold')
    body_style = ParagraphStyle('CustomBody', parent=styles['Normal'], fontSize=11, alignment=TA_JUSTIFY, spaceAfter=12)
    
    # === PAGE 1: COVER & SUMMARY ===
    story.append(Paragraph(f"📊 {t('pdf_title')}", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Dataset Info Box
    info_data = [
        [t('pdf_report_info'), ''],
        [t('pdf_generated'), datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        [t('pdf_total_resp'), str(len(data))],
        [t('pdf_x_vars'), ', '.join(x_items) if x_items else 'N/A'],
        [t('pdf_y_vars'), ', '.join(y_items) if y_items else 'N/A'],
    ]
    info_table = Table(info_data, colWidths=[2.5*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1565c0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#e3f2fd')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#1565c0')),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Executive Summary
    story.append(Paragraph(t('pdf_exec_summary'), heading_style))
    summary_text = f"""{t('pdf_exec_text_1')} {len(data)} {t('pdf_exec_text_2')} <b>{strength.lower()}</b> {direction.lower()} {t('pdf_exec_text_3')} {r:.3f}, {t('pdf_exec_text_4')} {p:.4f}). {t('pdf_exec_text_5')} <b>{t('pdf_statistically_sig') if p < 0.05 else t('pdf_not_statistically_sig')}</b> {t('pdf_exec_text_6')} ({method}) {t('pdf_exec_text_7')}"""
    story.append(Paragraph(summary_text, body_style))
    
    story.append(PageBreak())
    
    # === PAGE 2: DESCRIPTIVE STATISTICS ===
    story.append(Paragraph(f"1. {t('pdf_desc_stats')}", heading_style))
    
    # Loop through all analyzed variables
    for idx, col in enumerate(variables_to_analyze[:3]):  # Limit to first 3 for PDF space
        if col not in data.columns:
            continue
        
        story.append(Paragraph(f"{t('pdf_variable')} {col}", subheading_style))
        series = data[col]
        
        if pd.api.types.is_numeric_dtype(series):
            desc = descriptive_numeric(series)
            
            # Statistics table
            stats_data = [
                [t('pdf_statistic'), t('pdf_value')],
                [t('count'), str(desc[t('count')])],
                [t('mean'), f"{desc[t('mean')]:.2f}"],
                [t('median'), f"{desc[t('median')]:.2f}"],
                [t('std_dev'), f"{desc[t('std_dev')]:.2f}"],
                [t('min'), f"{desc[t('min')]:.2f}"],
                [t('max'), f"{desc[t('max')]:.2f}"],
            ]
            stats_table = Table(stats_data, colWidths=[2*inch, 2*inch])
            stats_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e3f2fd')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#0d47a1')),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
            story.append(stats_table)
            story.append(Spacer(1, 0.2*inch))
            
            # Save histogram to BytesIO and add to PDF
            try:
                fig_hist, ax_hist = plt.subplots(figsize=(6, 3))
                clean_data = series.dropna()
                ax_hist.hist(clean_data, bins=15, alpha=0.7, color='#1e88e5', edgecolor='white')
                ax_hist.set_title(f'{t("pdf_distribution")} {col}', fontsize=11, fontweight='bold')
                ax_hist.set_xlabel(col, fontsize=9)
                ax_hist.set_ylabel(t('frequency'), fontsize=9)
                ax_hist.grid(True, alpha=0.3)
                
                # Save to BytesIO instead of temp file
                img_buffer = BytesIO()
                fig_hist.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight')
                img_buffer.seek(0)
                plt.close(fig_hist)
                
                # Add image to PDF from BytesIO
                img = Image(img_buffer, width=5*inch, height=2.5*inch)
                story.append(img)
                story.append(Spacer(1, 0.2*inch))
                
            except Exception as e:
                story.append(Paragraph(f"<i>Chart generation error: {str(e)}</i>", body_style))
        
        if idx < len(variables_to_analyze) - 1:
            story.append(Spacer(1, 0.2*inch))
    
    story.append(PageBreak())
    
    # === PAGE 3: NORMALITY TESTING ===
    story.append(Paragraph(f"2. {t('pdf_normality_test')}", heading_style))
    story.append(Paragraph(t('pdf_normality_text'), body_style))
    story.append(Spacer(1, 0.1*inch))
    
    norm_data = [
        [t('variable'), t('p_value'), t('distribution'), t('pdf_interpretation_col')],
        ['X_total', f'{x_norm:.4f}', t('normal') if x_norm > 0.05 else t('non_normal'), 
         t('pdf_data_follows') if x_norm > 0.05 else t('pdf_data_not_follows')],
        ['Y_total', f'{y_norm:.4f}', t('normal') if y_norm > 0.05 else t('non_normal'),
         t('pdf_data_follows') if y_norm > 0.05 else t('pdf_data_not_follows')]
    ]
    norm_table = Table(norm_data, colWidths=[1.3*inch, 1*inch, 1.3*inch, 2.9*inch])
    norm_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e3f2fd')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#0d47a1')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(norm_table)
    story.append(Spacer(1, 0.2*inch))
    
    method_suitability = t('pdf_pearson_suitable') if method == t('pearson') else t('pdf_spearman_suitable')
    method_text = f"""<b>{t('pdf_selected_method')}</b> {t('pdf_method_text_1')} <b>{method}</b> {t('pdf_method_text_2')} {method_suitability}"""
    story.append(Paragraph(method_text, body_style))
    
    story.append(PageBreak())
    
    # === PAGE 4: CORRELATION ANALYSIS ===
    story.append(Paragraph(f"3. {t('pdf_corr_analysis')}", heading_style))
    
    # Correlation results table
    corr_data = [
        [t('pdf_metric'), t('pdf_value'), t('pdf_interp')],
        [t('method'), method, t('pdf_method_used')],
        [t('coefficient'), f'{r:.3f}', f'{strength} {direction.lower()} {t("pdf_relationship")}'],
        [t('p_value'), f'{p:.4f}', t('significant') if p < 0.05 else t('not_significant')],
        [t('pdf_sample_size'), str(len(data)), t('pdf_num_obs')],
    ]
    corr_table = Table(corr_data, colWidths=[2*inch, 1.8*inch, 2.7*inch])
    corr_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e3f2fd')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#0d47a1')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (1, -1), 'CENTER'),
        ('ALIGN', (2, 0), (2, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(corr_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Scatter plot with regression line
    story.append(Paragraph(t('pdf_scatter_plot'), subheading_style))
    try:
        fig_scatter, ax_scatter = plt.subplots(figsize=(6, 4))
        ax_scatter.scatter(data["X_total"], data["Y_total"], alpha=0.6, s=50, c='#1e88e5', edgecolors='white')
        
        # Add trend line
        z = np.polyfit(data["X_total"].dropna(), data["Y_total"].dropna(), 1)
        p_fit = np.poly1d(z)
        x_line = np.linspace(data["X_total"].min(), data["X_total"].max(), 100)
        ax_scatter.plot(x_line, p_fit(x_line), "r--", linewidth=2, alpha=0.8, label=t('pdf_trend_line'))
        
        ax_scatter.set_xlabel("X_total", fontsize=11, fontweight='bold')
        ax_scatter.set_ylabel("Y_total", fontsize=11, fontweight='bold')
        ax_scatter.set_title(f'{method}\nr = {r:.3f}, p = {p:.4f}', fontsize=12, fontweight='bold')
        ax_scatter.legend(fontsize=9)
        ax_scatter.grid(True, alpha=0.3)
        
        # Save to BytesIO instead of temp file
        scatter_buffer = BytesIO()
        fig_scatter.savefig(scatter_buffer, format='png', dpi=150, bbox_inches='tight')
        scatter_buffer.seek(0)
        plt.close(fig_scatter)
        
        # Add to PDF from BytesIO
        img_scatter = Image(scatter_buffer, width=5.5*inch, height=3.7*inch)
        story.append(img_scatter)
        
    except Exception as e:
        story.append(Paragraph(f"<i>Scatter plot error: {str(e)}</i>", body_style))
    
    story.append(PageBreak())
    
    # === PAGE 5: INTERPRETATION & CONCLUSION ===
    story.append(Paragraph(f"4. {t('pdf_interpretation')}", heading_style))
    
    substantial_or_moderate = t('pdf_substantial') if abs(r) > 0.5 else t('pdf_moderate')
    increase_or_decrease = t('pdf_increase') if r > 0 else t('pdf_decrease')
    direct_or_inverse = t('pdf_direct') if r > 0 else t('pdf_inverse')
    same_or_opposite = t('pdf_same_direction') if r > 0 else t('pdf_opposite_direction')
    sig_status = t('pdf_statistically_sig') if p < 0.05 else t('pdf_not_statistically_sig')
    reject_or_not = t('pdf_reject_null') if p < 0.05 else t('pdf_cannot_reject')
    association_type = t('pdf_sig_association') if p < 0.05 else t('pdf_an_association')
    
    interp_text = f"""{t('pdf_key_findings')}
    <br/><br/>
    <b>1. {t('pdf_strength_rel')}</b><br/>
    {t('pdf_strength_text_1')} {r:.3f} {t('pdf_strength_text_2')} <b>{strength.lower()}</b> {t('pdf_strength_text_3')} {substantial_or_moderate} {t('pdf_between_vars')}
    <br/><br/>
    <b>2. {t('pdf_direction_rel')}</b><br/>
    {t('pdf_direction_text_1')} <b>{direction.lower()}</b> {t('pdf_direction_text_2')} {increase_or_decrease}. {t('pdf_direction_text_3')} {direct_or_inverse} {t('pdf_direction_text_4')} {same_or_opposite}.
    <br/><br/>
    <b>3. {t('pdf_stat_sig')}</b><br/>
    {t('pdf_sig_text_1')} {p:.4f}, {t('pdf_sig_text_2')} <b>{sig_status}</b> (p {'<' if p < 0.05 else '≥'} 0.05). {t('pdf_sig_text_3')} {reject_or_not}.
    <br/><br/>
    <b>{t('pdf_important_note')}</b><br/>
    <i>{t('pdf_causation')} {association_type} {t('pdf_causation_text')}</i>
    """
    story.append(Paragraph(interp_text, body_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Conclusion
    story.append(Paragraph(f"5. {t('pdf_conclusion')}", heading_style))
    sig_or_not = t('significant') if p < 0.05 else t('not_significant')
    
    conclusion_text = f"""<b>{t('pdf_summary')}</b><br/><br/>
    1. <b>{t('pdf_desc_analysis_sum')}</b> {t('pdf_desc_text')} {len(variables_to_analyze)} {t('pdf_desc_text_2')}<br/><br/>
    2. <b>{t('pdf_composite')}</b> {t('pdf_composite_text')}<br/><br/>
    3. <b>{t('pdf_corr_analysis_sum')}</b> {t('pdf_corr_text_1')} {strength.lower()} {direction.lower()} (r = {r:.3f}) {t('pdf_corr_text_2')} {sig_or_not} {t('pdf_corr_text_3')}<br/><br/>
    4. <b>{t('pdf_method_rigor')}</b> {t('pdf_method_text')} ({method}) {t('pdf_method_text_2')}<br/><br/>
    5. <b>{t('pdf_academic')}</b> {t('pdf_academic_text')}<br/><br/>
    <b>{t('pdf_recommendations')}</b><br/>
    • {t('pdf_rec_1')}<br/>
    • {t('pdf_rec_2')}<br/>
    • {t('pdf_rec_3')}<br/>
    • {t('pdf_rec_4')}
    """
    story.append(Paragraph(conclusion_text, body_style))
    
    # Footer
    story.append(Spacer(1, 0.5*inch))
    footer_text = f"""<i>{t('pdf_footer')} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</i>"""
    story.append(Paragraph(footer_text, ParagraphStyle('Footer', parent=body_style, fontSize=9, alignment=TA_CENTER, textColor=colors.grey)))
    
    # Build PDF
    doc.build(story)
    pdf_buffer.seek(0)
    
    # Download button
    st.download_button(
        label=f"📥 {t('pdf_download_btn')}",
        data=pdf_buffer,
        file_name=f"statistical_analysis_full_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
        mime="application/pdf",
        type="primary",
        use_container_width=True
    )
    
    st.success(f"✅ {t('pdf_success')}")
    st.info(f"📊 {t('pdf_includes')}")
    
except ImportError:
    st.error("❌ ReportLab library not found. Install with: pip install reportlab")
except Exception as e:
    st.error(f"❌ Error generating PDF: {str(e)}")
    import traceback
    st.code(traceback.format_exc())

st.markdown("</div>", unsafe_allow_html=True)
