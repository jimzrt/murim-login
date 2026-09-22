<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0691.txt",
      "sha256": "92b57f4bc81b6a602382276c0f746a9eefa59d2ce78140e2c4ae900a29e6baf2",
      "bytes": 13033
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6e47f70112e933a18c475726c467964c4d051b9eaa0fc06a059c8a3534309eb7",
      "bytes": 1538
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3bd36033a8e83ea76cb8345710c858f69987095efab9064f44135007a7214e6b",
      "bytes": 204372
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "118ac824f0f243fedbfce6ccffd4e745781456960ab992776851bd5056138a36",
      "bytes": 781
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "97a3a4ba20b64c9b18a6751da155afe8456f4ca3e83b72026f4b64a271f49bc2",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "2e07f637ae3796cf2080cda259ea36ddf378583a6c8afddc22bbb83c2dfbfa31",
      "bytes": 784
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "28c33e09463a1a7212e1ce8589ff1e0df193bf92759ee89c821d8a089978e8a4",
      "bytes": 1897
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2f36631eeef4f889cf667edb266c507a6c1db7d0321026606396bb9bc612868e",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "cf0467976ce093edf3e279d0e40e576c790a7bbb083b3e9fbda5d6e56b6fba0a",
      "bytes": 687
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "c158eb3cccf55f61070b21bd808d359152479fbf7b53d1ebd43a710cc841aa1f",
      "bytes": 770
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "7f53d45a130cf8968b40c24cfa4e89173f717ef605f34f8736dd2fa0618ab12f",
      "bytes": 670
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "115fe2ab39ec79fd7d1f1bb0fcd8446da618315aade3f81fc34873c82e51fdf2",
      "bytes": 212668
    }
  ],
  "estimated_tokens": 11157
}
-->

# Durable State Update — Chapter 691

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 691. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 691. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 691,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 691,
    "continuity_sources": [691],
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
    "Yohi, Muyaho, and Jin Taekyung are trapped in a bright enclosed realm containing a pond that heals wounds.",
    "The Black Tiger saved and treated them but remains an unknown supernatural being that can vanish without a trace.",
    "Jin Taekyung has awakened after lying unconscious in the healing pond.",
    "Yohi trusts Jin Taekyung as a powerful and morally committed ally capable of helping Nanman.",
    "The Beast Miao King has been branded a traitor, fled the Nanman Beast Palace, and disappeared.",
    "Nanman is under general mobilization, the Miao leadership is imprisoned, and the Southern Heaven Demon Empress is nearing completion of her grand plan.",
    "Jin Taekyung has revisited the final childhood memory of his father in a dream altered by his adult consciousness."
  ],
  "continuity_sources": [
    690
  ],
  "open_questions": [
    "What is the Black Tiger, and who or what is its master?",
    "What is the bright healing realm, and how did Yohi, Muyaho, and Jin Taekyung reach it?",
    "Why is the Black Tiger helping them?",
    "What will Jin Taekyung reveal now that he has awakened?",
    "Can Yohi and the others return to Nanman before the Southern Heaven Demon Empress completes her plan?"
  ],
  "safe_through": 690,
  "temporary_decisions": [
    "Keep the Black Tiger distinct from the White Tiger.",
    "Treat the pond as a healing feature of the realm rather than an elixir.",
    "Render 아빠 as Dad in Jin Taekyung's childhood memory."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 아이템              | **Item**                       |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 오크 | **Orc** | Monster species. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 원정 | **Origin Essence** | The Water God Dragon's purified energy core, which humans call an inner core. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 흑호 | **Black Tiger** | A colossal black tiger that appears at the Ailao Mountain massacre site. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |
| 축골공 | **Bone-Shrinking Technique** | A martial art that stretches and shrinks bone and flesh to alter the user's appearance. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 야수묘왕 | 흑호 | hostile pursuer to unknown supernatural beast | you | blunt and furious | Directly challenges the Black Tiger over the massacre. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 요희 | 무야호 | human ally to intelligent spiritual beast | you | casual and familiar | Yohi asks Muyaho whether it wants her to ride on its back. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 690
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace and a Supreme Peak master who secretly lived for decades under Heugung's identity through the Bone-Shrinking Technique.
- **Personality:** The Beast Miao King is calculating, patient, ruthless, and willing to endanger Nanman's people to advance Dark Heaven's grand plan.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He maintained his public bond with Baeksang while secretly monitoring Baeksang and Yohi for the Southern Heaven Demon Empress, but he has now been branded a traitor, fled the Nanman Beast Palace, and disappeared.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 690
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 690
- **Aliases:** Beast Miao King
- **Role:** Heugung is the secret identity of the Beast Miao King, a Supreme Peak master and long-term Dark Heaven contingency who concealed himself through the Bone-Shrinking Technique.
- **Personality:** Heugung is calculating, patient, ruthless, and obsessive, masking coercion and strategic intent behind warmth and romantic devotion toward Yohi.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung is obsessed with Yohi and is willing to threaten her and the Yao people to force her compliance while secretly serving the Southern Heaven Demon Empress.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 690
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner who has awakened inside an unexplained healing realm after lying unconscious in its pond.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 690
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 690
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature currently sharing an unexplained healing realm with Yohi and Jin Taekyung.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 690
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is the strategist directing Baeksang's defense of Nanman's Inner and Outer Palaces while advancing a grand plan scheduled to begin within three days.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 690
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people, one of Nanman's four great tribes, and is currently separated from Heugung in an unexplained enclosed realm with her internal energy restored.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃691화



가끔 그럴 때가 있다.

그날 꾸었던 꿈이 너무나도 좋아서, 그리워서 깨고 싶지 않을 때가. 일어난 후에도 한참 동안 눈을 감고 그 꿈에서 있었던 일을 곱씹을 때가.

하지만 언제나 그렇듯, 세상 일은 내 바람대로 흘러가지 않는 법이다.

“진태경!”

- 크릉!

비명 같은 외침과 함께 달려드는 두 개의 크고 작은 신형. 곧 벌어질 일을 짐작하는 건 그리 어려운 일이 아니었다.

물론 그 일이 벌어지지 않게 하는 것도.

탁, 풍덩!

나는 신속하게 요희의 다리를 걸어 넘어트리고, 침을 질질 흘리며 다가오는 무야호의 주둥이를 밀어 냈다.

그리고 한마디와 함께 다시 눈을 감았다.

“삼 초. 삼 초만 건드리지 말아 봐.”

속으로 셋을 셌다. 아주 느리게, 꿈속에서 봤던 모든 것을 떠올리고 머릿속에 담고 다시 눈을 떴다.

동시에 밤인지, 낯인지조차 구분되지 않는 낯선 하늘이 시야에 들어온다.

‘낯선 하늘이라.’

이건 좀 신박하네.

심심하면 보는 하늘이 낯설 수 있나 싶지만, 두 눈으로 똑똑히 보고 있는 이상 틀림없는 사실이다.

나는 욱신거리는 몸을 일으키며 입을 열었다.

“우선 물어볼게. 혹시 기절한 사이에 암천이 남만을 접수했다, 뭐 그런 말을 하려는 건 아니지?”

연못에 넘어져 흠뻑 젖은 요희가 황당하다는 표정으로 되물었다.

“눈 뜨자마자 사람 발 걸어 놓고 하는 소리가 그거니?”

“눈 뜨자마자 달려드니까 발을 걸지. 그리고 하늘 봐라. 지옥이라고 해도 믿겠다.”

“지옥이면 어쩌려고?”

“글쎄.”

나는 주위를 둘러봤다.

맑은 물로 가득한 연못과 푸르른 초목(草木). 사방을 둘러싼 수풀 사이에서는 산새들의 지저귐과 짐승들의 호기심 어린 눈동자가 숨어 있다.

‘지옥치고는 경치가 너무 좋은데.’

내심 중얼거린 나는 어깨를 으쓱해 보였다.

“이미 뒈졌는데 뭘 어떡해. 잠이나 마저 자야지.”

“……잠을 자? 제정신이야?”

“아니. 사실 아직도 눈앞이 어질어질해.”

사실이다. 상반신을 일으킨 것만으로도 전신이 욱신거리고 현기증이 도니까.

뭐 그래도…….

“아직 살아 있는 것 같긴 하네. 확실하게.”

그래, 나는 또 다시 살아남았다.

지금 이 순간에도 엄습해 오는 고통과, 귓가에 울려 퍼지는 시스템 알림이 바로 그 증거다.

띠링.



확인하지 못한 알림 목록이 있습니다.

새로운 알림을 확인하시겠습니까?

Y / N



곧장 시스템 창을 확인하려던 나는, 문득 잊고 있던 사실을 떠올리고 고개를 돌렸다.

눈치를 보면서도 초롱초롱하게 빛나는 청백색 눈동자. 그리고 프로펠러처럼 돌아가는 꼬리를 보자 피식 웃음이 나온다.

“그래, 네 덕분에 살았다.”

- 크앙!

와락!

마치 그 말을 기다린 것처럼 무야호의 거대한 동체가 내게 달려들었다.

아직 완전히 회복되지 않은 몸뚱어리가 무게에 짓눌려 비명을 질러 댔지만 괜찮다. 이건 살아 있다는 걸 알려 주는 기분 좋은 통증이니까.

우두둑.

“……아.”

기분이 좀 안 좋아지려고 하네.



* * *



사실 암천이 아닌가 의심되는 무야호의 암살 시도는 다행히 미수에 그쳤고, 갈비뼈가 제자리에 있다는 걸 확인한 나는 가장 궁금한 점을 물었다.

“그런데 흑웅은? 왜 안 보여?”

동시에 볼 수 있었다. 흑웅이라는 두 글자가 나오기 무섭게 굳어 버린 요희의 얼굴을.

“그놈 얘기는 꺼내지도 마.”

“잠깐, 설마?”

“그래. 네가 생각하는 그게 맞아.”

“흑웅이 청혼했냐?”

“……!”

“미친놈일세. 아무리 좋아도 그렇지. 어떻게 그 상황에서 청혼을 하냐.”

나를 미친놈 보듯 응시하던 요희가 입술을 뗐다.

“우리가 알던 흑웅이 아니었어. 모두 속았던 거야.”

“그렇긴 하더라. 축골공 쓰니까 나름 훈훈하던데.”

“……축골공? 넌 알고 있었어?”

“알고 있었지. 나한테 밀서까지 보내서 만났었는데.”

“그럼 놈이 암천이 심어 놓은 세작(細作)이었다는 것도?”

“당연히 그것도 알고 있, 뭐?”

내가 지금 뭘 들은 거지.

잠시 고민하던 나는 무겁게 입을 열었다.

“사실이야?”

“거짓말하는 것처럼 보여?”

시벌, 사실인 모양이다.

동시에 이제야 문득 추종향 추적 퀘스트가 떠올랐다.

왜 시스템이 요희만 콕 집어 명시했었는지, 이제야 알 것 같은 기분이다.

“좋아. 흑웅 보고 훈훈하게 생겼다고 한 건 취소. 정중한 사과도 곁들여서.”

그 말은 하지 말걸.

훈훈이고 나발이고, 분위기는 싸늘하게 식은 지 오래. 요희가 한숨처럼 대답했다.

“상관없어. 덕분에 살았으니까.”

“아, 청혼 운운한 것도 추가로 사과할게.”

“괜찮아. 청혼한 건 사실이니까.”

“뭐?”

“사실이라고. 정확히는 청혼보다 명줄을 손아귀에 쥐고 흔드는 위협에 가까웠지만.”

“그, 혹시 승낙했어?”

“아까부터 묻고 싶었는데, 너 진짜 미친 새끼니?”

“어, 미안. 머릿속이 복잡해서 자꾸 말이 헛나오네.”

아직도 뒤통수가 얼얼하다.

한때는 흑웅을 의심했던 것도 사실이지만, 독혈지에서 두 노괴(老怪)와 맞닥트린 이후에는 그 약간의 의심마저 지워 버렸었으니까.

‘그런데 흑웅, 그 새끼가 암천의 끄나풀이었다니.’

결국 흑웅의 역할은 소매 속의 칼이었던 셈이다. 마지막의 마지막까지 염두에 둔 남천마후의 한 수.

그리고 이쯤에서 재차 드는 의문은, 도대체 어떻게 요희와 무야호가 그 한 수를 피했냐는 거였다.

앞서 요희가 한 말을 들어 보면 상당히 심각한 상황에 처했던 것 같은데.

“흑웅은 어떻게 됐지?”

“죽었어.”

잠시 생각하던 요희가 덧붙였다.

“아마도.”

“아마도?”

“우리도 자세한 사정은 몰라. 저 백호는 목숨이 경각에 달해 있었고, 나는 놈이 준 단환에 정신을 잃었으니까. 정신을 차려 보니 이곳이었어.”

이어지는 요희의 이야기는 짧았다. 이곳이 어디인지도, 바깥의 시간이 얼마나 흘렀는지도 모른다는 것.

그리고 분명 숨이 끊기기 직전이었던 무야호와 중상을 입은 나는 이 신비한 연못 덕분에 살아남았다는 것.

“이해해. 믿을 수 없는 헛소리 같겠지. 하지만 정말…….”

“이해했어.”

“뭐?”

“이해했다고. 전부 다.”

상처를 치유해 주는 연못이 뭐 그리 대수겠나.

이런 현상을 이해할 수 없는 건 이 세상 사람들에 한해서다.

나는 포션과 마법, 그리고 몬스터와 게이트가 존재하는 현대에서 왔고 지금 당장 저 풀숲 사이에서 오크 몇 마리가 기어 나와도 눈썹 하나 까딱하지 않을 자신이 있었다.

“…….”

다시 생각해 보니까 눈썹 정도는 까딱할 것 같다. 아무리 그래도 무림에서 오크가 나오는 게 정상은 아니니까.

‘현대에서처럼 진짜 게이트가 열린다면 모를까.’

스륵.

내심 중얼거린 나는 손을 뻗어 잔잔한 수면 위를 훑었다.

흡사 포션과도 같은 효력을 지닌 신비한 연못.

아마도 내가 정신과 육체에 쌓인 피로를 금방 털어낼 수 있었던 것은, 김좌진 장군마냥 등장한 아버지 덕분만은 아니었을 것이다.

‘아이템 감정.’

삐빅.



- 신비한 힘이 시스템을 거부합니다!

- 해당 목표를 파악할 수 없습니다!



이것 봐라.

어느 정도는 예상했지만, 역시 알 수 없는 것들 투성이다. 하나부터 아홉까지.

그리고 지금 막 요희의 입술 사이로 흘러나오는 열 번째 사실까지.

“흑호(黑虎)를 봤어. 지금껏 마주한 어떤 맹수보다 강하고, 특별하게 느껴지는 검은 호랑이를.”

“……!”

촤륵.

나도 모르게 흔들린 손끝이 서서히 가라앉던 수면을 뒤흔든다. 멀리 퍼져 나가는 파동을 바라보던 나는 신음을 삼켰다.

‘애뇌산의…… 망령(亡靈).’

단 한 번 봤지만 잊을 수 없었던 거대한 흑호가 뇌리를 스쳐 지나간다.

망령이라는 이름답게 유령과도 같이 나타나, 유령처럼 사라지던 놈의 모습이 아직도 생생하다.

‘그리고 그게 처음이자 마지막이었고.’

그날 밤, 나와 야수묘왕은 망령을 쫓던 과정에서 독혈지를 발견했지만 정작 놈의 모습은 그 어디에도 발견하지 못했다.

이는 천년지주와의 싸움이 끝난 직후 파견된 남만야수궁의 조사단도 마찬가지였고, 잇따라 벌어진 여러 굵직한 사건들로 인해 망령의 존재는 잠시 내 기억 저편에 머물러 있었다.

그런데 놈이 지금, 여기에서 등장할 줄이야.

‘심지어 정황을 보면 우리를 구해 준 게 틀림없는데.’

그 의도도, 정체도 모르겠다.

미간을 찌푸린 나는 마음속으로 중얼거렸다.

‘알림 확인.’

띠링.

오직 나만이 들을 수 있는 맑은 종소리와 함께, 꾹꾹 눌러 담아져 있던 홀로그램 창들이 허공으로 뛰쳐나왔다.



- 레벨 업!

- 레벨 업의 효과로 일부 부상이 회복됩니다!

- 레벨 업의 효과로 일부 상태 이상이 해제되었습니다!

- 매우 뛰어난 업적, [일 대 이의 전설]을 달성하셨습니다!

- 업적 달성 보상이 주어집니다!

- 보너스 포인트를 획득했습니다!

- 대량의 경험치와 명성치를 획득했습니다!

- 돌발 퀘스트, [소매 안의 칼]이 생성되었습니다!

- 돌발 퀘스트가 강제 취소되었습니다!

- [???]를 발견했습니다!

- 돌발 퀘스트, [???]가 대기 중입니다. 퀘스트 발동 조건을 모두 충족시켰을 시 진행됩니다.



이제야 확인했을 뿐. 내가 정신을 잃은 사이에도 시스템은 제 역할을 톡톡히 해냈다.

문제는 신처럼 전지전능한 시스템조차도, 내게 확실한 정보를 알려 주지 못했다는 점이다.

‘저 물음표가 더럽게 신경 쓰이는 건 정상이겠지.’

그리고 가장 신경 쓰이는 마지막 두 개의 알림을 뚫어져라 바라보고 있던 그때, 아까부터 자꾸 주위를 맴돌던 무야호가 내게 커다란 머리를 들이밀었다.

- 끄으응. 끙.

“똥 마렵니? 저기 가서 싸. 형 바쁘다.”

- 끼이이잉.

“바쁘다고 했…….”

문득 말을 멈춘 나는 불현듯 고개를 들었다. 동시에 똑똑히 볼 수 있었다.

연못을 둥그렇게 감싼 절벽 위, 아무런 기척도 없이 이곳을 내려다보는 어떤 존재를.

‘저건.’

그리고 내가 생각을 완성해 내기도 전에, 생각지도 못했던 음성이 머릿속에 울려 퍼졌다.

- 깨어났군. 인간.

“……!”

- 올라오너라. 할 이야기가 있다.

그 순간, 나는 불과 몇 달 전의 기억을 떠올렸다.

넓고 깊은 강물에서 용이 되지 못한 이무기가 내게 의념(意念)을 흘려보내던 그때를.



* * *



나는 홀로 절벽을 올랐다. 무야호도, 요희도 뒤에 남겨 둔 채.

그리고 성치 않은 몸으로 이끼에 뒤덮인 절벽 위에 올랐을 때, 마침내 어둠을 닮은 거대한 흑호 한 마리를 마주할 수 있었다.

애뇌산의 망령. 그래, 놈이었다.

“넌…… 뭐지?”

처음으로 흘러나온 한마디에, 흑호가 깊이를 알 수 없는 눈빛으로 나를 응시했다.

- 모른다.

“뭐?”

- 나조차도 모른다. 내가 무엇인지. 모든 걸 기억하기에는 너무 오랜 세월이 흘렀고, 그만큼 여러 이름으로 불렸지.

“……애뇌산의 망령.”

- 그 이름은 오랜만에 듣는군. 아마 이백여 년이었던가?

담담하게 의념을 흘려보낸 흑호가 걸음을 내딛는다.

분명 실체가 존재함에도 그 어떤 기척도, 소리도 전해지지 않는 유령 같은 움직임.

내가 전신의 털이 곤두서는 듯한 감각을 사로잡힌 그때. 의념이 이어졌다.

- 하지만 인간이여. 너는 알고 있을 것이다. 내가 어떤 존재인지를.

“…….”

- 부정한다 해도 소용없다. 나는 이미 너를 통해 그의 존재를 확인했으니.

천천히 돌아선 흑호가 입을 벌린다. 그 사이에 담긴 눈부시도록 푸르고 투명한 물체.

그것의 정체는 바로 수신룡의 원정이었다.

“이 새끼, 언제 훔쳐 갔어?”
```

## Final English reading copy

```markdown
# Chapter 691

Sometimes, that happens.

Sometimes a dream is so wonderful, so dearly missed, that you don't want to wake up. Sometimes, even after waking up, you keep your eyes closed for a long while, turning over everything that happened in the dream.

But as always, the world never goes the way I want it to.

“Jin Taekyung!”

—Grrr!

Two figures, one large and one small, came rushing at me with a cry that sounded almost like a scream. It wasn't difficult to guess what was about to happen.

Of course, preventing it from happening wasn't difficult either.

Thwack, splash!

I swiftly tripped Yohi, then shoved away Muyaho's muzzle as he approached, drooling all over himself.

Then I closed my eyes again after saying one thing.

“Three seconds. Don't bother me for just three seconds.”

I counted to three in my head. Very slowly, recalling everything I had seen in the dream and etching it into my mind before opening my eyes again.

At the same time, an unfamiliar sky entered my field of vision—a sky so strange that I couldn't even tell whether it was night or day.

*An unfamiliar sky, huh?*

That was pretty new.

You'd think the sky you saw whenever you were bored couldn't possibly feel unfamiliar, but there was no mistaking what I was seeing with my own two eyes.

I sat up with a throbbing body and opened my mouth.

“Let me ask you first. You're not about to tell me that Dark Heaven took over Nanman while I was unconscious or something, are you?”

Soaked from falling into the pond, Yohi looked incredulous as she asked,

“That's what you say after tripping someone the moment you open your eyes?”

“You came rushing at me the moment I opened my eyes, so I tripped you. And look at the sky. I'd believe you if you told me this was hell.”

“What are you going to do if it is?”

“Who knows?”

I looked around.

A pond filled with clear water and lush vegetation. Hidden among the bushes surrounding us on every side were the chirping of mountain birds and the curious eyes of wild animals.

*The scenery is too nice for hell.*

I muttered inwardly and shrugged.

“I’m already dead, so what else can I do? I might as well finish sleeping.”

“……Sleep? Are you in your right mind?”

“No. In fact, everything is still spinning in front of my eyes.”

It was true. Just sitting up made my entire body throb, and dizziness washed over me.

Still…

“I do seem to be alive. Definitely.”

Yes, I had survived once again.

The pain assailing me even now and the System notifications ringing in my ears were proof of that.

Ding.



> **System**
>
> There are unconfirmed notifications.
>
> Would you like to check the new notifications?
>
> Y / N



I was about to check the System window right away when I suddenly remembered something I had forgotten and turned my head.

Bright blue-white eyes that shone despite watching me warily. And when I saw the tail spinning like a propeller, I let out a quiet laugh.

“Yeah. I survived thanks to you.”

—Kraaang!

With a whoosh!

As though he had been waiting for me to say those words, Muyaho's enormous body charged at me.

My not-yet-fully-recovered body screamed as it was crushed beneath his weight, but it was all right. This was a pleasant pain that reminded me I was alive.

Crack.

“……Ah.”

This was starting to feel a little less pleasant.

* * *

Fortunately, Muyaho's assassination attempt—which had made me suspect he might actually be Dark Heaven—ended in failure. After confirming that my ribs were still in place, I asked what I was most curious about.

“But what happened to Heugung? Why can't I see him?”

At the same time, I saw Yohi's face stiffen the moment the name Heugung left my lips.

“Don't even mention that bastard.”

“Wait. Don't tell me…”

“That's right. It's exactly what you're thinking.”

“Heugung proposed to you?”

“……!”

“What a lunatic. No matter how much he likes you, how could he propose in that situation?”

Yohi stared at me as if I were the crazy one, then finally parted her lips.

“He wasn't the Heugung we knew. We were all deceived.”

“That was true. He was pretty easy on the eyes with the Bone-Shrinking Technique.”

“……The Bone-Shrinking Technique? You knew?”

“Of course I knew. He even sent me a secret letter and met with me.”

“Then did you also know that he was a spy planted by Dark Heaven?”

“Of course I knew that too, wha—?”

What had I just heard?

After thinking for a moment, I opened my mouth heavily.

“Is that true?”

“Do I look like I'm lying?”

*Fuck. Looks like it was true.*

Only then did I suddenly remember the Quest to track the tracking scent.

Now I understood why the System had singled out and explicitly named only Yohi.

“All right. I retract saying Heugung looked pleasant. Along with a formal apology.”

I should not have said that.

To hell with whether he looked pleasant or not—the mood had long since turned ice-cold. Yohi answered with a sigh.

“It doesn't matter. I survived thanks to him.”

“Oh, and I'll apologize for bringing up the proposal too.”

“It's all right. He did propose.”

“What?”

“I said it's true. More accurately, it was less a proposal than a threat to toy with my life in the palm of his hand.”

“Th-Then did you accept?”

“I've been meaning to ask this for a while, but are you actually insane?”

“Uh, sorry. My head's a mess, so I keep saying stupid things.”

The back of my head was still throbbing.

It was true that I had once suspected Heugung, but after running into the two old monsters in the Poisonblood Grounds, I had erased even that slight suspicion.

*But Heugung, that bastard, was Dark Heaven's lackey?*

In the end, Heugung had been the knife in the sleeve—a move the Southern Heaven Demon Empress had kept in reserve until the very end.

And the question that came to me again at this point was how Yohi and Muyaho had managed to avoid that move.

Judging from what Yohi had said earlier, they had been in a fairly serious situation.

“What happened to Heugung?”

“He's dead.”

After thinking for a moment, Yohi added,

“Probably.”

“Probably?”

“We don't know the details either. That White Tiger was at death's door, and I lost consciousness from the pill he gave me. When I came to, I was here.”

The rest of Yohi's story was short. They didn't know where this place was or how much time had passed outside.

And Muyaho, who had clearly been on the verge of death, and I, who had suffered severe injuries, had survived thanks to this mysterious pond.

“I get it. It must sound like unbelievable nonsense. But really…”

“I understand.”

“What?”

“I said I understand. All of it.”

What was so remarkable about a pond that healed wounds?

Only people of this world would be unable to understand such a phenomenon.

I had come from the modern world, where potions, Magic, monsters, and Gates existed. Even if a few Orcs crawled out from those bushes right now, I was confident I wouldn't bat an eye.

“……”

On second thought, my eyebrow might twitch a little. No matter how you looked at it, Orcs appearing in the Murim wasn't normal.

*Unless a real Gate opened, like in the modern world.*

I muttered inwardly and reached out to skim the calm surface of the water.

A mysterious pond with an effect much like a potion.

The reason I had been able to shake off the fatigue piled up in my mind and body so quickly probably wasn't only because of my father, who had made an entrance like General Kim Jwa-jin.[^1]

*Item Appraisal.*

Beep.



> **System**
>
> —A mysterious power rejects the System!
>
> —The target cannot be identified!



See?

I had expected it to some extent, but as I thought, everything was a mystery. From one to nine.

And now, a tenth fact slipped between Yohi's lips.

“I saw a Black Tiger. A black tiger that felt stronger and more extraordinary than any wild beast I had ever encountered.”

“……!”

Splash.

My trembling fingertips disturbed the surface of the water, which had been slowly settling. I swallowed a groan as I watched the ripples spread into the distance.

*The apparition of Ailao Mountain…*

The enormous Black Tiger, which I had seen only once but could never forget, flashed through my mind.

It had appeared like a ghost, true to the name apparition, and vanished like one as well. Its image remained vivid even now.

*And that had been the first and last time.*

That night, the Beast Miao King and I discovered the Poisonblood Grounds while pursuing the apparition, but we couldn't find a trace of it anywhere.

The investigation team from the Nanman Beast Palace, dispatched immediately after the battle with the Thousand-Year Spider, had met with the same result. Then, because of the string of major incidents that followed, the apparition's existence had temporarily receded to the back of my mind.

And yet it had appeared here.

*What's more, judging from the circumstances, it definitely saved us.*

I didn't know its intention or its identity.

Frowning, I muttered inwardly.

*Check notifications.*

Ding.

With a clear bell only I could hear, holographic windows that had been held back burst into the air.



> **System**
>
> —Level Up!
>
> —Some injuries have recovered due to the effects of Level Up!
>
> —Some Status effects have been removed due to the effects of Level Up!
>
> —You have achieved the exceptional achievement **The Legend of One Against Two**!
>
> —The achievement Reward has been granted!
>
> —You acquired bonus points!
>
> —You acquired a large amount of EXP and Fame!
>
> —A sudden Quest, **The Knife in the Sleeve**, has been created!
>
> —The sudden Quest has been forcibly canceled!
>
> —You discovered **???**!
>
> —A sudden Quest, **???**, is pending. It will proceed once all activation conditions have been met!



I was only checking them now. Even while I had been unconscious, the System had done its job perfectly.

The problem was that even the System, which was as omniscient as a god, couldn't provide me with any definite information.

*It's normal for those question marks to bug the hell out of me, right?*

As I stared intently at the last two notifications—the ones that bothered me most—Muyaho, who had been circling me for a while, thrust his enormous head at me.

—Nnngh. Ngh.

“Do you need to poop? Go over there and do it. Hyung's busy.”

—Whiiine.

“I said I was bu—”

I suddenly stopped speaking and raised my head.

At the same time, I saw it clearly.

Something was looking down at this place from atop the cliffs encircling the pond, without giving off the slightest hint of its presence.

*That's…*

Before I could finish the thought, an unexpected voice rang out inside my head.

—You've awakened, human.

“……!”

—Come up. We have something to discuss.

At that moment, I remembered something from only a few months earlier.

The time when an imugi that had failed to become a dragon sent a thought into my mind from within a broad, deep river.



* * *

I climbed the cliff alone, leaving Muyaho and Yohi behind.

When I reached the moss-covered cliff with my battered body, I finally came face-to-face with a massive Black Tiger that resembled darkness itself.

The apparition of Ailao Mountain.

Yes—it was the same one.

“What are you…?”

At my first words, the Black Tiger stared at me with eyes of unfathomable depth.

—I don't know.

“What?”

—Even I don't know what I am. Too much time has passed for me to remember everything, and I have been called by many names in that time.

“……The apparition of Ailao Mountain.”

—I haven't heard that name in a long time. Was it around two hundred years ago?

The Black Tiger calmly sent the thought and took a step.

Though it clearly possessed a physical body, it moved like a ghost, without transmitting the slightest presence or sound.

Just as I was seized by the sensation that every hair on my body was standing on end, the thought continued.

—But, human. You know what kind of being I am.

“……”

—Denying it won't help. I have already confirmed his existence through you.

The Black Tiger slowly turned and opened its mouth.

Nestled between its jaws was an object that shone with dazzling blue transparency.

It was the Water God Dragon's Origin Essence.

“When the hell did you steal this, you bastard?”

[^1]: Kim Jwa-jin (1889–1930) was a Korean independence activist and military commander.
```
