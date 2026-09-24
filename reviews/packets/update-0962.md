<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0962.txt",
      "sha256": "9b87ea1d87ce9492f9102297f9bcf9f80a22f24ff525f7eb3a764bb5326c9f29",
      "bytes": 14545
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8fa4868cef8320e566eb7223816805468ebe09c529cefdfab5a8c81e469493b8",
      "bytes": 2400
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d2cd41a475ca2207576e960da5e1a472021261aaf33a057d240c294fea49f839",
      "bytes": 235187
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "ea50d5bd78e358d40e54e88ed2182f00d7d4e574d074ee7a4f8f3fa495b47549",
      "bytes": 1005
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "445b8f416ef18e09fdf693db3ccfeb1906196f68fe00e89253f94149b492617f",
      "bytes": 709
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "221449d93504b0ad0e5aaa2ed904a559892c044d038ff758069fa55f5a140b65",
      "bytes": 759
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "a9dc996d01b204fadc06ec513d84214b2cad87eb82d39c6d8c2323936a6e20e2",
      "bytes": 1343
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "4f411a82aca7275c3b78c6e2ea6803ef7da4607921df5fda9d7dcd375fb26d1f",
      "bytes": 1095
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "a6fa6f66eb6f776c153350e3e18bf709c7b8079d86d74b0769a3e315571d1d4d",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f3891a6f1dc69b187910650fe3f1d1ef0807d3efb213de9337d593761b5d84c5",
      "bytes": 268981
    }
  ],
  "estimated_tokens": 11337
}
-->

# Durable State Update — Chapter 962

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 962. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 962. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 962,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 962,
    "continuity_sources": [962],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The battle at Eight Spring Gorge continues; Jin Mukyung, Wipeng, and Cheol Mubaek are fighting the Demon Bird amid the Shanxi defenders’ battle against the steppe army.",
    "The Demon Bird is an elderly, overwhelmingly powerful martial artist who wore Chinggen’s face and left Temur alive to control the western tribes.",
    "The Demon Bird is also known as the Blood Soul Fat Demon; he severed both arms of Cheol Mubaek’s master, the Fist Hero.",
    "Cheol Mubaek and Wipeng are badly injured but still fighting; their weapons are made from the Water God Dragon’s bones, not Ten-Thousand-Year Cold Iron.",
    "The Demon Bird has left an opening, and a swordsman’s attack is descending; its result is not yet known.",
    "Jamukha ordered the Keshik at the gorge to wear down the defenders while limiting losses to his personal guard; three of his commanders of a hundred have died.",
    "Temur chose survival over loyalty and feels guilty that his actions led his followers to slaughter; Jamukha threatened him into obedience.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    961
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge end, and what will be the result of the swordsman’s attack on the Demon Bird?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Temur and the followers he led into battle?"
  ],
  "safe_through": 961,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 철무백    | **Cheol Mubaek**   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 생도     | **cadet**                                    |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 노부      | **this old man / I**                                            |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 검기상인 | **the level of injuring others with Sword Energy** | Realm description used for Moon Beauty Saber. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 검기성강 | **Sword Energy Becoming Force** | Supreme Peak realm in which Sword Energy has entered the Force stage. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |
| 혈혼비마 | **Blood Soul Fat Demon** | The Demon Bird’s former sobriquet, which he resents. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 칭겐 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | The impostor wearing Chinggen’s face addresses Jamukha with deference. |
| 진무경 | 마조 | hostile opponents | you | blunt and insulting | Mukyung directly insults the Demon Bird, refusing to call him Master. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 961
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** His master, the Fist Hero, was a great fist master whose arms were severed by the Blood Soul Fat Demon; he is a close friend and peer of Lee Cheonbaek, a paternal uncle and protector of Lee Seowol, and considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival.

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 959
- **Aliases:** None
- **Role:** The real Chinggen, a Khan of the eastern grasslands and Temur’s sworn brother, is dead; the impostor who wore his face has revealed himself as the Demon Bird, an elderly and overwhelmingly powerful martial artist.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur was Chinggen’s cousin and sworn brother through the anda oath; the impostor who killed Chinggen and wore his face spared Temur to control the western tribes.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 961
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 961
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Peak-level swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 959
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he can agonize over costly decisions but commits firmly once resolved.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 961
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃962화



찰나를 쪼개고 쪼갠 짧은 시간 속, 마조는 깨달았다.

이제 자신에게 남은 선택지는 하나뿐이라는 사실을.

솨악.

마치 유령처럼 다가와 나직이 귓가에 닿은 희미한 파공성.

그와 동시에 세상이 느려졌다.

모든 것이 선명했다.

극심한 내상을 입은 위팽과 철무백의 엷은 숨결도, 그들의 입술 사이로 쏟아져 내리는 핏방울도.

그리고 마조는, 마침내 굳게 말아쥐고 있던 두 자루의 애병을 놓으며 돌아섰다.

온 힘을 다해 땅을 박참과 동시에, 벼락같은 쌍장(雙掌)을 내지르며.

화악!

양손을 휘감으며 번뜩이는 핏빛 강기.

만근거석조차 단숨에 가루로 만들어 버릴 거대한 기운은 막힘없이 나아갔다.

마조의 머리 위로 떨어져 내리는, 바다를 닮은 푸르른 검기(劍氣)를 향해.

그 칼날 같은 검기의 파도를 몰고 온 한 사람을 향해.

진무경.

태원진가의 젊은 검귀(劍鬼)와 일평생 숱한 살업을 쌓아 올린 늙은 마인(魔人)의 시선이 허공에서 맞닿는다.

서로를 조금도 닮아 있지 않은 두 사람이었다.

지금껏 살아온 일생도, 타고난 시대도, 마음에 품은 뜻도.

청년은 그저 검이 좋아 무공을 익혔고, 노인은 누군가를 죽이기 위해 검을 휘둘렀다.

청년은 힘을 원했다. 몰락해 가는 가문을 일으켜 세우기 위해.

노인은 힘을 갈망했다. 강해질수록 더 많은 이들을 짓밟을 수 있으니까.

청년은 난세(亂世)를 원치 않는 수많은 이들 중 한 사람이었으나, 노인은 핏물이 강이 되어 흐르고 시체가 산처럼 쌓였던 과거의 그 시절을 누구보다 그리워했다.

지금껏 걸어온 길도, 앞으로 나아가야 할 방향도 달랐다.

바로 이 순간, 두 사람이 서로를 향해 내뻗은 검기와 장력이 토해 내는 소리조차도.

쉭.

푸른 파도처럼, 혹은 한 줄기의 벼락처럼 쏟아진 검기는 어린아이의 숨소리처럼 희미했고.

콰아아!

거대한 핏빛 장력은 천둥처럼 으르렁거렸다.

그리고 그 작은 차이점 사이에는 지금까지의 모든 것을 합친 것만큼이나 깊고 넓은 간격이 존재했다.

누군가는 바람을 뭉갰고, 누군가는 바람을 갈랐으니까.

고오오옹.

아득한 섬광. 들끓는 공기.

각기 다른 두 개의 붉고 푸른 빛이 서로를 향해 치닫는 그 광경을 바라보며, 마조는 불현듯 생각했다.

초절정과 절정.

검기성강(劍氣成罡)과 검기상인(劒氣傷人)이라 불리는 그 두 경계선에 놓인 깨달음의 벽은, 어쩌면 자신이 생각했던 것만큼 높고 거대하지 않았을지도 모른다는 생각을.

‘이건…….’

마조는 휘몰아치는 광풍 속에서도 또렷하게 빛나는 푸른빛을 바라보았다.

흔들림 없이 정해진 궤적을 따라 비스듬히 내리그어진 그 일격은, 한 청년이 지금까지 얻은 모든 깨달음과 새로운 경지로 나아가는 진보(進步)의 증거이기도 했다.

우우웅.

마침내 맞닿은 두 개의 거대한 기운이 바람을 지웠다.

공간을 일그러트렸다.

그리고 전신을 갈가리 찢어 버릴 것 같은 그 엄청난 압력 속에서, 진무경은 눈을 감았다.

달빛조차 흐린 깊은 밤.

시야가 차단되자 비로소 내려앉은 칠흑 같은 어둠.

너무나도 익숙했다. 전신의 모든 기운과 감각이 들끓어 올라 손에 쥔 한 자루의 검을 향해 흘러 들어갔다.

아무것도 보이지 않았으나, 느껴졌다.

당장이라도 모든 것을 휩쓸어 버릴 듯한 상대의 강대한 힘이.

흉포하지만 그렇기에 불안정한 장력의 틈새가.

그래.

‘저곳이다.’

진무경은 홀린 듯이 검을 내리그었다. 고요하게 내려앉은 눈꺼풀 사이를 비집고 흘러들어온 푸른 빛은, 그 어느 때보다 선명했다.

천 번, 만 번. 혹은 그것의 수십, 수백 배.

헤아릴 수도 없이 두드리고 식힌다면 하잘것없는 잡철(雜鐵)도 언젠가는 훌륭한 명검으로 변모한다.

어디선가 떨어진 물 한 방울이 단단한 바위를 깨트리고, 코끼리를 쓰러트리는 것은 발바닥에 박힌 가시 하나다.

바로 지금처럼.

솨아아악.

마조는 똑똑히 보았다.

예리하다 못해 한 줄기의 실선처럼 보이는 푸른 섬광이, 자신의 장력을 좌우로 가르는 믿을 수 없는 광경을.

동시에 찬탄했다.

‘아.’

속도, 힘, 궤적.

그 모든 것이 눈부셨다. 소름이 끼칠 만큼 완벽했다.

더는 검기라 부를 수 없는 저 예리함이, 핏빛 강기를 가르며 나아가는 신병이기(神兵利器)가 뿜어내는 섬광이.

‘실로, 아름답구나.’

미처 토해 내지 못한 그 한 마디와 함께, 마조는 환하게 웃었다.

그리고 자신의 머리 위로 쏟아져 내리는 푸른 빛줄기를 향해, 떨리는 두 손을 뻗었다.

서걱.

아름답고도 눈부신 그 파도는, 몸서리칠 만큼 차가웠다.



* * *



세상이 멈췄다.

아니, 정확히는 모두의 움직임이 멈췄다.

감히 폭군이나 다름없는 상관의 싸움에 관여하지 못한 채 전투를 이어 가던 유목민들도, 끊임없이 몰려드는 군세에 조금씩 지쳐가던 산서인들도.

끊어지려는 정신을 간신히 붙잡고 있는 것만이 고작인, 전장의 그 누구보다 가까운 곳에서 모든 것을 지켜본 철무백과 위팽 역시도 예외는 아니었다.

서걱.

조금 전, 유난히도 선명하게 울려 퍼진 한 줄기의 절삭음은 아직도 그들의 귓가에 맴돌고 있었다.

이해하지 못할 의문과 함께.

‘도대체…….’

‘무슨 일이 벌어진 거지?’

모두의 뇌리를 스친 생각.

아득하게 부풀어 오르는 섬광 속에서 붉고 푸른 빛이 번뜩였고, 그것이 전부였다.

전장의 모두가 그 휘황한 빛을 똑똑히 보았으나, 동시에 아무것도 보지 못했다.

지금 이 순간.

핏물과 시체로 가득한 이 비좁은 협곡에 내려앉은 침묵을 깨트릴 수 있는 것은, 일 장의 거리를 사이에 둔 채 서로를 등지고 선 두 사내뿐이었다.

진무경과 마조.

마조와 진무경.

오랜 세월에 걸쳐 무수한 살업을 쌓아 올린 늙은 마인과, 지난 이 년간 칠흑 같은 어둠 속에서 한 자루의 검을 휘두르던 젊은 검귀는 천천히 서로를 향해 돌아섰다.

철벅.

무거운 발걸음과 함께 누구의 것인지 모를 핏물이 웅덩이에서 흘러넘친다.

그리고 이내, 누군가의 새로운 피가 그 빈자리를 메웠다.

쿨럭.

온 힘을 다해 악물고 있던 입술이 벌어진다.

마치 금이 간 둑이 허물어지듯, 그 미세한 틈새로 내장 조각이 뒤섞인 핏물이 터져 나왔다.

촤아아악.

허공을 수놓은 검붉은 액체가 지면을 적신다. 다시 채워진 피 웅덩이에 비친 것은 창백하게 질린 젊은 검귀의 얼굴이었다.

- 안 돼! 무경아!

카카캉!

저 멀리 들려오는 누군가의 다급한 외침과 함께 다시 울려 퍼지기 시작하는 강철의 소음.

익숙한 목소리의 주인을 떠올리며 흐릿하게 웃는 진무경을 향해, 마조가 문득 입을 열었다.

“무엇이냐, 그 일검은.”

그가 느낀 모든 감정과 의문을 담기에는 너무나도 짧은 한마디.

다시 한번 울컥 솟구치는 핏물을 삼킨 진무경이 대답했다.

“나도 모른다. 그런 것은 처음이라.”

마조가 실소를 흘렸다.

비웃음이 아니었다. 자신조차 잊은 무아(無我)의 상황에서 새로운 경지로 발돋움한 이들은 늘 같은 대답을 하곤 했으니까.

소싯적의 그 역시도.

“솔직하군.”

“어쩔 수 없지. 그것이 사실이니까.”

“한 번. 마지막으로 한 번만 더 네 녀석의 일검을 볼 수 있다면 얼마나 좋을까.”

“사양하지. 네놈 면상이라면 이미 지긋해.”

마조의 입가에 맺힌 웃음이 더욱 짙어졌다.

“그 초식의 이름은 지었느냐?”

진무경이 조용히 고개를 저었다.

그가 수련한 것은 무공인 동시에, 어떤 의미로는 무공이 아니었으니까.

오직 일격(一擊).

단 하나의 검로를 찾기 위해 이 년의 세월을 바쳤고 오늘 이 자리에서 그 끝자락을 잠시 엿봤을 뿐.

그렇기에 초식명 따윈 생각해 본 적도 없었다.

눈앞의 노괴가 말을 꺼내기 전까지는.

“청파낙조(靑波落鳥).”

푸른 파도가 몰아치니, 한 마리 새가 떨어진다.

싯구를 읊듯이 중얼거린 마조는 진무경을 향해 의기양양한 어조로 물었다.

“어때, 제법 훌륭하지 않으냐?”

“글쎄. 좀 유치한데.”

“이런.”

마조의 안색 위로 실망감이 번지던 그때, 진무경이 담담한 목소리로 말을 이었다.

“하지만 뭐, 그것도 익숙해지면 나름대로 괜찮을 것 같군.”

“그래? 역시 그렇지?”

마조는 입이 찢어져라 웃었다.

자신의 전신 곳곳에 희미하게 드러나기 시작한 붉은 실선의 존재를 까맣게 모른 채.

아니, 애써 모르는 척하며.

“진천검(振天劍) 진무경. 태원진가의…… 쿨럭, 어린 검귀여.”

투둑, 투두둑.

점점이 떨어지는 핏물.

진무경을 구하기 위해 달려들던 산서인들도, 상관의 승리를 확신하며 높은 사기로 그들을 막아내던 초원인들도 순간 크게 뜨인 눈으로 마조를 바라보았다.

비틀거리는 신형을 다잡으며, 진무경만을 응시하고 있는 늙은 마인을.

“죽여라. 죽이고, 또 죽여라.”

그의 눈빛과 목소리는 일평생을 다해 지켜온, 오직 살인에 대한 집념으로 불타오르고 있었다.

“노부를 벤 그 일검으로. 네놈을 막아서는 것들을 모조리. 크륵. 모조리……!”

스륵.

그러나 마조의 목소리는 끝까지 이어지지 못했다.

그의 몸 곳곳을 가로지른 붉은 실선이, 몽글몽글하게 피어오른 핏방울이 마침내 화려하게 폭발했기 때문이었다.

푸화아아악!

허공을 물들이며 솟구치는 피 분수.

썩은 고목 나무처럼 허물어지는 마조의 모습에 모두가 경악으로 눈을 부릅떴다.

쓰러진 자와 서 있는 자.

누가 승자고 패자인지는 명백하다.

상반신은 물론 양팔이 잘려 나간 상태로 자신이 만들어 낸 피 웅덩이에 머리를 박고 쓰러진 시체를 내려다보며, 진무경은 나직이 입을 열었다.

본격적인 전투가 시작되기 전, 마조가 했던 그 말을 그대로 돌려주며.

“저승에 가거든, 어느 한 산서인에게 죽었다 전해라.”

그리고 그 어느 때보다 무겁게 느껴지는 칼자루를 쥐고, 망설임 없이 적의 수급을 베어 모두를 향해 치켜들었다.

서걱.

“나, 태원진가의 진무경이 혈혼비마(血魂肥魔)를 베었다!”

“……!”

“……!”

얼마 남지 않은 공력이 실린 그 힘찬 외침에 협곡 안의 공기가 얼어붙었다.

이미 마조의 정체를 익히 알고 있던 자무카의 친위대들은 그의 최후에 경악했고, 오래전 천하를 피로 물들였던 마두의 별호를 들은 산서인들은 눈을 부릅떴다.

마조의 죽음.

그와 더불어 지금 이 순간, 새롭게 탄생한 또 한 명의 초절정 고수.

와아아아아아!

거대한 함성이 협곡 안을 뒤흔들었다. 용암이 터져 나오듯 피가 들끓어 오른 산서인들은 목숨을 도외시하며 달려들었다.

이 예상치 못한 상황에 얼어붙어 있던 친위대와 자신들의 대족장인 칭겐과 혈혼비마와의 연관성에 혼란스러워하는 후미의 유목민들을 단숨에 집어삼킬 듯이.

“쳐라!”

“우리는! 산서인들은 쓰러지지 않는다!”

“감히 이 땅을 침범한 오랑캐들을 모조리 쓸어 버려라!”

“발시(發矢)!”

쉬쉬쉬쉬쉭!

쏟아지는 화살 비 아래, 눈시울이 붉게 충혈된 진위경을 필두로 한 수천의 무림인과 관군은 송곳이 되어 허물어진 전열을 파고들었다.

“놈들이 온다!”

“방패! 방……!”

푸푸푹! 콰드드득!

잠시 가라앉았던 피 안개가 자욱하게 피어올랐다.

단숨에 뒤집힌 분위기 속, 사기가 최고조에 달한 산서인들은 죽음을 무릅쓰고 달려들었다.

젖 먹던 힘을 다해 병장기를 휘두르고, 고통을 참아내며 숨이 끊기는 그 순간까지 적들을 물어뜯었다.

서걱, 우지직!

하나를 베어 내면 둘이, 둘을 베어 내면 셋이.

그리고 이 다음은 없다. 남아 있는 것은 죽음뿐이다.

콰직!

열 중 일곱이 일류의 실력자들로 이루어진 케식은 명실상부한 초원의 최정예였지만, 협곡에 투입된 삼백여 명의 병력이 절반으로 줄어드는 것은 순식간이었다.

“어떻게, 이제 어떻게 해야 합니까!”

케식 십인장은 수하의 외침에 대답하지 않았다.

아니, 대답할 수 없었다.

세 명의 백인장도, 자무카와 더불어 또 하나의 절대자나 다름없던 마조도 죽었다.

그뿐인가.

이 순간에도 사방에서 날아드는 칼날에 수하들이 목숨을 잃고 있다.

그리고 그 중심에, 비틀거리는 신형으로 무수한 피를 집어삼키는 한 귀신이 있었다.

쉭, 서걱!

내리긋고, 베고, 찌른다.

진무경이 보인 그 단순한 움직임에 스무 명이나 되는 케식이 쓰러졌다.

극심한 내상을 입었음이 분명함에도, 태원진가의 검귀는 협곡의 한 가운데에서 자신들의 두 동료를 지켜 내고 있었다.

‘이게 무슨…….’

케식 십인장은 질끈 눈을 감았다.

그리고 이내, 짧은 망설임 끝에 후퇴 명령을 내렸다.

아니, 정확히는 내리려고 했다.

바로 그 순간, 등 뒤에서 울려 퍼진 익숙한 울림을 듣기 전까지는.

부우우우!

십인장은 알고 있었다.

수십여 개의 뿔피리가 동시에 토해 내는 그 거대한 울림은, 오직 한 사람을 위한 것이라는 사실을.

자무카.

위대한 칸이자, 초원의 절대자.
```

## Final English reading copy

```markdown
# Chapter 962

In that brief instant, split into ever smaller fragments, the Demon Bird realized that he had only one choice left.

*Shwaa.*

A faint whistle of displaced air reached him like a ghost, brushing softly against his ear.

At the same time, the world slowed.

Everything was clear.

The faint breaths of Wipeng and Cheol Mubaek, both suffering severe Internal Injuries. The drops of blood spilling from between their lips.

And then the Demon Bird finally released the two beloved swords he had been gripping tightly and turned around.

He kicked off the ground with all his strength, thrusting both palms forward like a bolt of lightning.

*Fwoosh!*

A flash of blood-red Force curled around his hands.

The tremendous energy, enough to reduce even a boulder weighing ten thousand *geun* to dust in an instant, surged forward without resistance.

Toward the sea-blue Sword Energy falling over the Demon Bird’s head.

Toward the man who had brought that blade-sharp wave of Sword Energy crashing down.

Jin Mukyung.

The eyes of the young Sword Demon of the Jin Family of Taiyuan and the old fiend who had spent his life piling up countless killings met in midair.

The two men couldn’t have been less alike.

Not in the lives they had led, the eras they had been born into, or the ideals they held in their hearts.

The young man had learned martial arts simply because he loved the sword. The old man had wielded one to kill.

The young man had wanted strength so he could raise his declining family back up.

The old man had craved strength because the stronger he became, the more people he could trample underfoot.

The young man was one of the countless people who wanted no part of an age of chaos. The old man longed more than anyone for those days gone by, when rivers of blood flowed and corpses piled up like mountains.

The paths they had walked, and the directions they had to go from here, were different.

Even the sounds of the Sword Energy and palm force they sent at each other in this very moment were different.

*Shhk.*

The Sword Energy fell like a blue wave—or a single bolt of lightning. It was as faint as a child’s breath.

*RROOOAR!*

The enormous blood-red palm force roared like thunder.

And between those small differences lay a gulf as deep and wide as everything that had come before.

One of them crushed the wind. The other cut through it.

*Gooooom.*

A distant flash. Air seething with heat.

Watching the two different lights—one red, one blue—race toward each other, the Demon Bird suddenly thought:

Supreme Peak and Peak.

The walls between the insights known as Sword Energy Becoming Force and the level of injuring others with Sword Energy might not have been as high and imposing as he had once believed.

*This is…*

Even amid the raging gale, the Demon Bird looked at the blue light shining clearly.

That unwavering strike, descending at an angle along its destined path, was proof of all the enlightenment the young man had gained so far—and of his progress toward a new realm.

*Rumble.*

At last, the two enormous forces met and erased the wind.

They warped space.

And under that tremendous pressure, enough to tear his whole body apart, Jin Mukyung closed his eyes.

A deep night, when even the moonlight was dim.

With his sight cut off, pitch-black darkness settled over him.

It was so familiar. Every bit of energy and sensation in his body surged and flowed into the sword in his hand.

He couldn’t see a thing, but he could feel it.

The opponent’s overwhelming power, ready to sweep everything away.

The gaps in his ferocious, but therefore unstable, palm force.

*Yes.*

*There.*

As if entranced, Jin Mukyung swept his sword down. Blue light slipped between his calmly closed eyelids, clearer than ever.

A thousand times, ten thousand times—or dozens, hundreds of times more.

Strike and cool it beyond counting, and even worthless scrap iron will one day become a fine sword.

A single drop of water from somewhere can crack a solid rock. A single thorn in an elephant’s foot can bring it down.

Just as it was now.

*Shwaaaash.*

The Demon Bird saw it clearly.

A blue flash, so sharp it looked like a single thread, split his palm force from side to side. It was unbelievable.

And at the same time, he marveled.

*Ah.*

Speed, power, trajectory.

Every part of it was dazzling. Perfect enough to make his skin crawl.

The divine weapon’s flash—no longer sharpness that could be called Sword Energy—cut through the blood-red Force and pressed onward.

*Truly beautiful.*

With that one word, left unspoken, the Demon Bird smiled brightly.

Then he reached out both trembling hands toward the blue streak of light falling over his head.

*Shhk.*

That beautiful, dazzling wave was cold enough to make him shudder.

* * *

The world stopped.

No—in truth, everyone stopped moving.

The nomads kept fighting, not daring to interfere in the battle of their superior, who was practically a tyrant. The Shanxi defenders, gradually tiring against the endless waves of enemy troops.

Not even Cheol Mubaek and Wipeng were spared. They had watched everything from closer than anyone else on the battlefield, barely managing to hold on to their fading consciousness.

*Shhk.*

The single, unusually clear slicing sound from moments ago still rang in their ears.

Along with a question they couldn’t understand.

*What on earth…?*

*What just happened?*

The same thought had crossed everyone’s mind.

Red and blue light had flashed within a distant, swelling blaze of light. That was all.

Everyone on the battlefield had seen that dazzling light clearly, and at the same time, no one had seen a thing.

At that moment, only the two men standing with a *jang* between them, their backs to each other, could break the silence that had settled over the narrow gorge, thick with blood and corpses.

Jin Mukyung and the Demon Bird.

The Demon Bird and Jin Mukyung.

The old fiend, who had spent a lifetime accumulating countless killings, and the young Sword Demon, who had spent the past two years swinging a sword in pitch-black darkness, slowly turned to face each other.

*Splash.*

With a heavy step, a pool of blood—no one knew whose—overflowed onto the ground.

And soon, fresh blood from someone filled the space it had left.

*Cough.*

His lips, clenched with all their strength, parted.

Like a cracked dam giving way, a spurt of blood mixed with pieces of his innards burst through that tiny gap.

*Splaaash!*

Dark red liquid painted the air and soaked the ground. Reflected in the pool of blood, now filled again, was the pale face of the young Sword Demon.

—No! Mukyung!

*CLANG!*

Along with someone’s desperate cry from far away, the clamor of steel began to ring out again.

Thinking of the familiar voice behind that cry, Jin Mukyung smiled faintly. The Demon Bird suddenly spoke to him.

“What was that strike?”

It was far too short to contain all the feelings and questions he had.

Jin Mukyung swallowed another surge of blood and answered.

“I don’t know, either. It was the first time.”

The Demon Bird let out a dry laugh.

It wasn’t mockery. Those who stepped into a new realm in a state of selflessness, forgetting even themselves, always gave the same answer.

He had, when he was young, too.

“Honest, at least.”

“Can’t help it. It’s the truth.”

“If only I could see that strike of yours one more time. Just once, before the end.”

“I’ll pass. I’ve had more than enough of your face.”

The smile on the Demon Bird’s lips grew wider.

“Have you named that form?”

Jin Mukyung quietly shook his head.

What he had trained in was martial arts, and at the same time, in a sense, it wasn’t.

Only One Strike.

He had spent two years searching for a single path for his sword, and today, in this place, he had glimpsed its very edge.

He had never even considered giving it the name of a form.

Not until the old monster in front of him spoke.

“Blue Wave, Falling Bird.”

A blue wave surges, and a bird falls.

Murmuring as if reciting a line of poetry, the Demon Bird asked Jin Mukyung with a self-satisfied air:

“Well? Pretty good, isn’t it?”

“Hard to say. It’s kind of cheesy.”

“Oh.”

Disappointment spread across the Demon Bird’s face. Then Jin Mukyung continued, his voice calm.

“But I guess it might grow on me.”

“Really? I knew you’d see it my way.”

The Demon Bird grinned from ear to ear.

He had no idea that faint red lines were beginning to appear all over his body.

No—he was making an effort to pretend he hadn’t noticed.

“Heaven Shaking Sword, Jin Mukyung. Of the Jin Family of Taiyuan… Cough, you young Sword Demon.”

*Drip. Drip.*

Blood fell in scattered drops.

The Shanxi defenders rushing to save Jin Mukyung, and the steppe fighters who had been holding them back with high morale, certain of their superior’s victory, stared at the Demon Bird with wide eyes.

At the old fiend who steadied his swaying frame and kept his eyes fixed on Jin Mukyung alone.

“Kill them. Kill them, and kill them again.”

His eyes and voice burned with the obsession he had held onto all his life: the desire for nothing but murder.

“With that strike you used to cut me down. Anything that stands in your way—every last one. Guh… Every last one…!”

*Slith.*

But the Demon Bird’s words never reached their end.

The red lines crossing his body, and the beads of blood swelling along them, finally burst in a magnificent explosion.

*FWOOSH!*

A fountain of blood surged upward, staining the air.

Everyone’s eyes widened in shock as the Demon Bird collapsed like a rotten tree.

One man fallen, one man still standing.

It was clear who had won and who had lost.

Looking down at the corpse sprawled face-first in the pool of blood he had made, his upper body and both arms severed, Jin Mukyung spoke in a low voice.

He returned the very words the Demon Bird had said before the battle began.

“When you get to the afterlife, tell them a man from Shanxi killed you.”

Then, gripping the hilt that felt heavier than ever, he cut off his enemy’s head without hesitation and raised it for all to see.

*Shhk.*

“I am Jin Mukyung of the Jin Family of Taiyuan! I have slain the Blood Soul Fat Demon!”

“……!”

“……!”

His powerful shout, backed by the little internal energy he had left, froze the air in the gorge.

Jamukha’s personal guard, already well aware of the Demon Bird’s identity, was stunned by his end. The Shanxi defenders stared wide-eyed at the title of the fiend who had stained the world with blood long ago.

The Demon Bird’s death.

And, at the same time, a new Supreme Peak master.

“Waaaaah!”

A tremendous roar shook the gorge. The Shanxi defenders, their blood boiling like lava bursting forth, charged forward, heedless of their lives.

They looked ready to swallow the personal guard, still frozen by the unexpected turn of events, and the nomads in the rear, bewildered by the connection between their Great Chieftain Chinggen and the Blood Soul Fat Demon.

“Attack!”

“We are Shanxi! We will not fall!”

“Wipe out every barbarian who dared invade this land!”

“Loose!”

*Shh-shh-shh-shshsh!*

Beneath a downpour of arrows, thousands of martial artists and government troops, led by Jin Wikyung with his eyes red and bloodshot, drove like a wedge into the broken enemy line.

“They’re coming!”

“Shields! Sh—!”

*Puhpuhpuk! KRRUNCH!*

The blood mist, briefly settled, rose thickly again.

The Shanxi defenders, their morale at its peak as the tide turned in an instant, charged forward, risking their lives.

They swung their weapons with every last ounce of strength, and endured the pain, biting at their enemies until their final breath.

*Shhk! CRUNCH!*

For every one they cut down, two took their place. For every two, three.

And there would be no next time. Only death remained.

*CRUNCH!*

Seven out of every ten Keshik were First Rate warriors. They were, without question, the finest troops on the grasslands. Yet in no time at all, the roughly three hundred men deployed in the gorge had been cut in half.

“What do we do? What are we supposed to do now?”

The Keshik squad leader didn’t answer his subordinate’s desperate shout.

No—he couldn’t.

The three commanders of a hundred were dead. So was the Demon Bird, another absolute master on a level with Jamukha.

And that wasn’t all.

Even now, his men were dying to blades flying at them from every direction.

And at the center of it all was a ghost, staggering as he drank in blood without end.

*Shhk. Shhk!*

He brings the sword down, cuts, thrusts.

With those simple movements, Jin Mukyung felled twenty Keshik.

Despite his clearly severe Internal Injury, the Sword Demon of the Jin Family of Taiyuan stood in the middle of the gorge, protecting his two companions.

*What is this…?*

The Keshik squad leader squeezed his eyes shut.

Then, after a brief hesitation, he gave the order to retreat.

Or, more precisely, he was about to.

Until he heard the familiar sound that rang out behind him.

*Boooooo!*

The squad leader knew what it meant.

That great sound, blown from dozens of horns at once, was meant for only one man.

Jamukha.

The great Khan, the supreme ruler of the grasslands.
```
