/// <reference types="vite/client" />

/**
 * Declare the module to load all .vue files
 */
declare module '*.vue' {
    import type { DefineComponent } from 'vue'
    // eslint-disable-next-line @typescript-eslint/ban-types, @typescript-eslint/no-explicit-any
    const component: DefineComponent<{}, {}, any>
    export default component
}

export * from '@/router/types'

/**
 * This interface enable the intelli-sense for .env
 * defined variables that would be used across the project
 */
interface ImportMetaEnv {
    readonly VITE_BACKEND_URL: string
}

/**
 * Interface that is used by Vite to inject
 * meta data on imports.
 */
interface ImportMeta {
    readonly env: ImportMetaEnv
}
