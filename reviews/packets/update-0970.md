<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0970.txt",
      "sha256": "8a65dcb8750bf4dbb06ab4960b6eba6ee9b299eef3a7e3af524b3bee58022f64",
      "bytes": 13491
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5d6b71800a77abee9f922d9e3c36ada70ee4ec74197366efd4fe322cb71eb857",
      "bytes": 1711
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "65892110351fce017f8020b13720d8c5e71418799da1db239060ea308ecc01e4",
      "bytes": 235501
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "bbb1989353af3fb3af4c6c6ec27795eb60e982aa2bf15a5588131fb463e1192a",
      "bytes": 1005
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "09b346c452d509776334304a171841a6f3f42b21c39ca8b4b5db15d3e771cf73",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7a29672c6ce9f3b5399e9f37850408d05b12739b8ecf21d5f947fe122ede1341",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "7462e1c3c4798b88bf9af21ebf057048551792e7775b517377ba3f2e72503213",
      "bytes": 667
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "2bfb5708b6b19acfb8af2e15800e5f16de89b1d19f7baa0b5a02e4bfd0634170",
      "bytes": 1389
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "1f27bbd18b699fd6dd8b3dc5e4d085026012c4fd6a9fb8980baf410654371892",
      "bytes": 911
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e4d65007963906e76cb9c90c4dc320901b3492379f327a0148926fbb16dc946d",
      "bytes": 270295
    }
  ],
  "estimated_tokens": 10485
}
-->

# Durable State Update — Chapter 970

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
1 and safe_through 970. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 970. Profile updates may replace only one
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
  "chapter": 970,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 970,
    "continuity_sources": [970],
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
    "Murong Baek spared Jamukha decades ago, recruited him into Dark Heaven, and now directs his military role.",
    "Murong betrayed his longtime friend Peng Cheolhu and intends to kill him; Peng is alive beneath the rubble.",
    "Murong plans to ambush the arriving Huashan and Zhongnan reinforcements and eliminate witnesses to Dark Heaven's actions.",
    "Jamukha did not take the improved Temporary Strength Pill, whose severe addictive effects make it unsuitable for him; his shoulder is nearly half severed.",
    "Jin Mukyung, Cheol Mubaek, and Wipeng are beneath the collapsed cliff; their condition is unresolved.",
    "An unidentified spear bearing blue-white flames has interrupted Murong's attack.",
    "The identity of the larger organization’s awakened figure and its plan remain unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment requiring him to die once remains unresolved.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown."
  ],
  "continuity_sources": [
    969
  ],
  "open_questions": [
    "Who wielded the blue-white-flamed spear, and what happens to the people beneath the rubble?",
    "What is Murong Baek’s full plan for Dark Heaven and the arriving reinforcements?",
    "Who is the awakened figure behind Jamukha’s recruiter, and what is the larger organization’s plan?",
    "What are the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 969,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 철무백    | **Cheol Mubaek**   |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 저승사자 | **Grim Reaper** | Mungyeong's threatening self-description during the banter. |
| 황하 | **Yellow River** | River along which civilization began. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 육부 | **Six Ministries** | The central government ministries. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 969
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** His master, the Fist Hero, was a great fist master whose arms were severed by the Blood Soul Fat Demon; he is a close friend and peer of Lee Cheonbaek, a paternal uncle and protector of Lee Seowol, and considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 960
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 969
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 955
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 969
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 969
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung and a longtime sword mentor to Jin Mukyung, whom he taught as a boy. He remains alert to threats connected with Dark Heaven, and the Human Butcher has claimed him as a personal target.

## Korean source

```text
＃970화



한 치 앞을 분간할 수 없는 흐릿한 어둠 속에서, 진무경은 눈이 아닌 마음으로 그의 앞에 놓인 단 하나뿐인 길을 직시하고 있었다.

미래이면서, 미래일 수 없는 그것.

영원한 죽음을.

‘끝이군.’

진무경 자신조차 놀랄 만큼, 지금 이 순간 현실을 받아들이는 그의 마음은 차분했다.

이미 최선을 다했으니까.

하늘을 우러러 한 점 부끄럽지 않을 만큼, 온 힘을 다해 싸웠고 마침내 그 힘이 다했으니까.

혼(渾)과 신(身).

그 모든 것을 쏟아부었다. 남은 것은 없다.

느려진 세상 속에서 천천히 들어 올려지는 한 자루의 창이, 그 창날에 깃든 죽음이 다가오는 것을 알면서도 손가락 하나 까딱하지 못할 정도로.

그럼에도 아직 마음 깊숙한 곳 어딘가에 남아 있는 한 줄기의 후회가 있다면, 그것은 바로 이승에 남아 있을 이들에 대한 것이리라.

‘이제 어떻게 되는 걸까.’

사후(死後)의 세상 따위는 아무래도 좋다.

지금 당장 검은 도포로 전신을 둘러싼 창백한 얼굴의 저승사자가 나타나, 그를 쇠사슬로 포박하여 염라대왕 앞에 세운다 해도 상관없다.

한 사람의 무인으로, 태원진가의 이 공자로 떳떳한 삶을 살았으니.

누군가를 죽이기 위해서가 아니라, 지키기 위해 쌓아 올린 살업(殺業)이었으니.

그러나 이제는 떠나야 한다.

모두를 뒤로 한 채, 알려지지 않은 어둠 너머로 끌려가야만 한다.

자의가 아닌 타의로.

지키고자 했으나, 끝끝내 지키지 못한 모든 것들을 이곳에 남겨 두고서.

‘……안 돼. 그것만은.’

그 순간, 진무경은 이를 악물었다.

서서히 잠겨 가는 의식을 억지로 일깨우며, 흘러나오지 않는 외침을 마음속으로 토해 냈다.

최선?

무엇이 최선이란 말인가.

어찌 이토록 나약하게 죽음을 받아들이려 했단 말인가.

아직 살아 있다면, 숨이 끊기기 전까지는 끝난 것이 아니다.

그는 일어나야 했다. 고동치는 심장의 박동이 멎는 그 순간까지 맞서 싸워야 했다.

‘나는, 나는……!’

손끝이 파르르 떨린다.

악문 잇새로는 비릿한 혈향이 풍겼다.

그러나 진무경이 스스로 혀를 깨물면서까지 일으켜 세우고자 했던 몸뚱어리는 이미 한계에 다다른 지 오래였고, 잔인한 현실은 변하지 않았다.

쉬익.

귓가를 파고드는 파공성이 선명하다. 흐릿하게 물든 시야 속, 비스듬히 떨어져 내리는 섬광은 유난히도 느리게 느껴졌다.

지금껏 살아온 일생을 반추(反芻)할 수 있을 만큼.

더불어 세상에서 가장 밉살맞기 그지없는, 누군가의 얼굴을 떠올릴 수 있을 만큼.

‘만약 나 대신 네 녀석이 이 자리에 있었다면…… 달라졌겠지. 모든 것이.’

진무경은 머리 위로 떨어져 내리는 창날을 바라보며, 어디에도 닿지 않을 공허한 목소리를 마음속으로 흘렸다.

지금 이 자리에 없는, 자신의 하나뿐인 아우에게.

‘아무래도 그 약속, 못 지킬 것 같다.’

이 년 전, 두 형제는 수련동의 벽을 사이에 두고 약속했다.

성라대연(星羅大宴).

천하를 수놓은 무수한 별들의 연회에서 만나자고.

그리고 그날의 약속을, 진무경은 끝끝내 지키지 못했다.

부끄러웠기 때문이었다. 진무경 스스로가 느끼는 자신의 성취가 턱없이 부족해서였다.

처음 검을 들었을 무렵에는 훌륭한 무인이 되고 싶었고, 그 이후에는 태원진가의 긍지이자 자랑스러운 아우가 되고 싶었다.

하지만 지난 이 년이라는 시간 동안, 그가 숨 막히는 어둠 속에서 쉬지 않고 검을 휘둘렀던 가장 큰 이유는 따로 있었다.

떳떳한 형이 되고 싶었다.

신룡(神龍)이 되어 훨훨 날아가는 아우가 부끄러워하지 않을 만큼, 청풍이라는 벽을 넘어설 만큼 강해지고 싶었다.

그러나…….

‘결국, 이렇게 되는군.’

진천검(振天劍) 진무경.

또 다른 괴물들에 가려진, 젊은 천재에게 주어진 기회의 시간은 이제 끝났다.

어둠 속에서 갈고닦은 그의 검은 오늘 이 협곡을 환하게 밝힐 만큼 눈부셨으나, 그 찰나의 빛줄기는 길고 깊은 밤에 파묻혀 사라질 것이다.

영원히.

‘빌어먹을.’

진무경은 반쯤 감겨 있던 눈꺼풀을 힘겹게 들어 올렸다.

다가오는 죽음에도 눈을 감지 않는 것은 그에게 남은 무인으로서의 긍지이자 꺾이지 않은 투지요, 동시에 골칫덩어리 아우에게 마지막 인사를 건네기 위함이다.

비록, 그 목소리가 어디에도 닿지 않을지라도.

“……미안하다.”

그리고 진무경의 입술 사이로 간신히 쥐어 짜낸 음성이 흘러나온 바로 그 순간.

꽈아아아앙!

하늘이, 땅이 뒤흔들렸다.

어둡고 흐릿하기만 하던 진무경의 세상이 청백색으로 물들고, 그의 머리 위로 떨어져 내리던 섬광이 방향을 꺾어 휘둘려졌다.

어느덧 빛보다 빠르게, 굉음조차 앞질러 들이닥친 끔찍한 열기를 향해.

아니, 끔찍한 열기가 실린 한 자루의 창을 향해.

고오오옹.

바람이 지워졌다. 공기가 멈췄다.

찰나의 순간 서로를 향해 맞닿은 두 줄기의 기운이 반경 수십여 장을 감싸 안으며, 이내 크게 부풀어 올랐다.

콰아아아아!

귓가를 먹먹하게 만드는 굉음과 함께 협곡 내부를 가로지르는 거대한 충격파.

깊게 파인 구덩이 속에 쓰러져 있던 진무경은 본능처럼 손을 뻗었다.

이미 혼절한 철무백과 위팽의 신형을 온 힘을 다해 부여잡은 채, 폭풍우에 휩쓸리듯 사방으로 날아가는 인마(人馬)의 시체와 무수한 암석의 파편을 보았다.

주위의 모든 것을 휘감은 그 아득한 섬광 속에서, 흐릿하게 보이는 누군가의 뒷모습도 함께.

쿨럭.

검붉은 핏물을 토해 낸 진무경은 문득 생각했다.

어쩌면 자신은 이미 죽었을지도 모른다고.

살아생전의 미련 때문에 죽어서도 헛것을 보고 있는 것이라고.

하지만…….

‘아니야.’

생생했다.

망자(亡者)에게 허락된 것이라고는 믿을 수 없을 만큼, 지금 이 순간 그가 보고 듣고 느끼는 모든 것이.

암석의 파편이 할퀴고 지나간 피부에서 올라오는 쓰라린 통증도. 비명을 질러 대는 전신의 근육과 극심한 내상으로 뒤틀린 오장육부에서 솟구치는 핏물도.

마지막으로, 그의 귓가로 흘러들어온 누군가의 낯익은 목소리도.

“뭘 그렇게 토악질을 해. 어제 과음이라도 했나.”

그 순간, 진무경의 신형이 덜컥 굳었다.

튀어나올 듯이 크게 뜨인 두 눈동자에는 격랑이 휘몰아쳤다.

확실하다.

환각이 아니다. 환청도 아니다.

이건, 이건…….

“등이라도 좀 두드려 주고 싶은데. 상황이 상황이라 그건 안 되겠네.”

가라앉아가는 굉음 너머로 또렷하게 들렸다.

서서히 희미해지는 섬광 속에서 선명하게 보였다.

듣는 것만으로도 주먹이 들어 올려지는, 저 밉살맞기 짝이 없는 목소리가.

언제부터인가 자신보다 넓고 단단한 등을 갖게 된 망나니의 뒷모습이.

“너……!”

도대체 어디서 그런 힘이 솟아오른 것일까.

진무경은 쇳소리가 섞인 목소리를 쥐어 짜내며 손을 들었다.

이미 한계를 벗어나 사시나무처럼 떨리는 손끝으로, 하나뿐인 아우의 옷자락을 향해 뻗었다.

스륵.

귀를 기울여야만 들을 수 있는 아주 작은 마찰음.

그 순간, 넝마가 된 장포의 끝자락을 스친 것은 진무경의 손길이 아닌 바람이었을지도 모른다.

하지만 그것으로 충분했다.

그가 전하고자 한 것은, 단순한 손길이 아닌 모두를 지켜 달라는 간절한 염원이었으니.

툭.

힘없이 떨어지는 손길. 축 늘어지는 전신.

그러나 마침내 모든 힘을 다하고 의식을 잃어버린 못난 형의 앞에는, 이 년간의 외유를 끝내고 돌아온 망나니 아우가 우뚝 서 있었다.

십여 장 밖에서 깊게 가라앉은 눈빛으로 자신을 응시하는, 낯선 얼굴을 한 반백의 중년인을 마주한 채.

“하나만 묻자.”

화염이 줄기줄기 쏟아지는 안광. 그에 반하여 얼음장처럼 차가운 목소리.

“네가, 우리 형 팼냐?”

탕아(蕩兒)가 돌아왔다.

하늘을 떨어 울리는 용이 되어서.

나직한 음성 너머로, 산서인들이 목놓아 내지르는 울음 섞인 환호가 울려 퍼지고 있었다.



* * *



얼마 전, 누군가 내게 말했다.

모든 것을 홀로 짊어지지 말라고.

그들을 조금 더 믿어 보라고.

그리고 지금 이 순간, 나는 깨닫고 있었다.

그 말이 옳았다는 것을.

전장에 도착하자마자 알 수 있었다.

사방이 피바다였다. 이름 모를 누군가의 몸뚱어리에서 떨어져 나간 팔다리가, 헤아릴 수도 없을 만큼 수많은 말과 사람의 시체가 작은 동산을 이루며 비좁은 협곡 안에 가득 차 있었다.

그리고 그중 대부분은 유목민들의 것이었다.

어림잡아도 최소 두 배 이상의 적.

단순한 머릿수를 떠나 전력 면에서도 확연하게 밀리는 상황에서도 산서인들은 꺾이지 않았다.

아니, 오히려 온 힘을 쥐어 짜내어 적들과 맞섰다.

관군도, 무림인도, 심지어는 무공이라면 일초반식조차 익히지 못했을 양민도.

마지막으로, 진무경도.

‘최선을 다한 거야. 죽음에 대한 두려움마저 떨쳐 내면서.’

약자가 강자에 대항하는 것이 얼마나 어려운 것인지, 나는 이미 알고 있다.

그런 그들의 희생이 더는 있어서는 안 된다는 진무경의 염원도 확실하게 이어받았다.

우우웅. 쾅!

손을 뻗자, 굉음과 함께 암벽 깊숙이 파고들었던 한 자루의 창이 살아 있는 생물처럼 몸을 비틀어 내게 다가온다.

짧은 여행을 끝마치고 되돌아온 백염(白炎)이 손아귀 안에서 작게 몸을 떨었다.

창날을 휘감은 청백색의 화염은 칠흑 같은 어둠을 밝히는 동시에, 차가운 밤공기를 뜨겁게 달구며 눈앞의 적을 향해 넘실거렸다.



[Lv.??? 모용백]



유목민들이 사용하는 돌격창과 흡사한 형태의, 거무튀튀한 색의 창을 그러쥔 채 우뚝 서 있는 반백의 중년인.

예리하게 날 선 [기감]으로 읽어 낸 그 시스템 창을 보았을 때, 내심 당황하지 않았다면 거짓말이지만 눈앞의 현실은 곧 진실이다.

나는 가라앉은 눈빛으로 그를, 지금껏 이름만 들어 보았던 모용세가의 가주를 바라보았다.

암천이 중원 무림이라는 거대한 숲에 숨겨 두었던 또 하나의 칼날, 북천마군(北天魔君)을.

“물었잖아. 네가 우리 형 팼냐고.”

잠시 침묵하던 북천마군이 입술을 뗐다.

“이거 참.”

전신을 훑는 눈빛. 초대하지 않은 불청객의 방문에 놈은 작게 한숨을 내쉬었다.

“골치 아프게 됐군. 여러모로.”

그럴 거다. 여러모로.

나는 언제든지 출수(出手)할 수 있게 창날을 곧추세우며 대답했다.

“왜 골치가 아프고 그러냐. 보는 사람 걱정 되게.”

지금의 내게 모용세가의 가주가 어떤 이유로, 언제부터 암천의 주구가 되었는지는 중요하지 않다.

내가 해야 할 일은 단 하나, 북천마군임이 틀림없는 모용백과 그 뒤에서 한껏 굳은 얼굴을 한 유목민을 쓰러트리는 것뿐이다.

“그러니까 이참에 그냥 골을 깨부수는 거 어때. 더 아플 일도 없게.”

저벅.

한 걸음을 내디디며, 북천마군이 담담한 어투로 대꾸했다.

“처음 듣는 치료법이로군.”

“내가 보기보다 의술에 조예가 있어. 신의(神醫) 옆에서 보고 배웠거든.”

“글쎄. 그렇다고 해도 그 방법은 아마 곤란할 것 같은데.”

모든 것을 꿰뚫어 보는 듯한 투명한 시선으로, 북천마군이 나를 바라보며 덧붙였다.

“지금 같은 상태로는 더더욱.”

부정하고 싶지만, 놈의 판단은 정확했다.

잠도, 식사도, 운기조식도 제대로 하지 못한 채 장장 만 리에 달하는 거리를 가로지르기 위해서 그만한 대가를 치러야 했으니까.

그래서 나는 망설임 없이 대답했다.

“뭐, 그건 그렇지.”

저벅.

조금씩 거리를 좁혀 오던 발걸음이 불현듯 멈춘다. 북천마군이 미간을 찌푸리며 나를 바라보았다.

“뭐라고?”

“네 말이 맞다고. 솔직히 이대로는 좀. 아니, 상당히 빡세지.”

“그게 무슨…….”

흐려지는 말꼬리. 나는 미친놈 보듯이 바라보는 북천마군을 향해, 어깨를 으쓱해 보였다.

“그래서, 겸사겸사 아는 사람 좀 데려왔지.”

그리고 그 말의 의미를 북천마군이 깨닫기도 전에, 두 줄기의 파공성이 휘몰아쳤다.
```

## Final English reading copy

```markdown
# Chapter 970

In the hazy darkness where he couldn’t see an inch ahead, Jin Mukyung stared—not with his eyes, but with his heart—at the only path laid out before him.

A future that couldn’t be the future.

Eternal death.

*So this is the end.*

Even Jin Mukyung was surprised by how calmly he accepted reality in that moment.

He’d already done everything he could.

He’d fought with all his strength, enough to look up at the heavens without a shred of shame. At last, that strength had run out.

Body and soul.

He’d poured everything into the fight. There was nothing left.

In a world that had slowed to a crawl, he couldn’t even twitch a finger as a spear rose slowly and the death dwelling in its blade drew near.

And yet, if a thread of regret still remained somewhere deep in his heart, it was for those he would leave behind in this world.

*What will happen to them now?*

He didn’t care what the afterlife was like.

Even if a pale-faced Grim Reaper, dressed head to toe in black, appeared right now, bound him in chains, and dragged him before Yama, it wouldn’t matter.

He had lived an honorable life as a martial artist, as the Jin Family of Taiyuan’s Second Young Master.

The blood on his hands had come from protecting others, not from a desire to kill.

But now he had to leave.

He had to leave everyone behind and be dragged beyond the unknown darkness.

Not by his own choice, but by someone else’s.

Leaving here everything he had wanted to protect, but in the end had failed to save.

*…No. Anything but that.*

In that instant, Jin Mukyung clenched his teeth.

He forced his fading consciousness awake and screamed silently in his heart.

Everything he could?

What did that even mean?

How could he accept death so weakly?

If he was still alive, then it wasn’t over until his last breath was gone.

He had to get up. He had to fight until the very moment his pounding heart stopped.

*I—I…!*

His fingertips trembled.

The taste of blood filled his mouth between his clenched teeth.

But the body he’d tried to rouse, even by biting his own tongue, had long since reached its limit. The cruel reality didn’t change.

*Whoosh.*

The sound of something cutting through the air rang clearly in his ears. In his blurred vision, the slanting flash seemed unusually slow.

Slow enough for him to look back on his entire life.

Slow enough for him to think of the most irritating person in the world.

*If you’d been here in my place… things would’ve been different. Everything.*

As the spearhead fell toward his head, Jin Mukyung sent his words into the void, where they would reach no one.

To his only younger brother, who wasn’t here.

*Looks like I won’t be able to keep that promise after all.*

Two years ago, the brothers had made a promise with the wall of the training hall between them.

They’d meet at the Star-Array Grand Banquet.

At the feast of countless stars that illuminated the world.

In the end, Jin Mukyung had failed to keep that promise.

Because he’d been ashamed. Because he felt his own achievements were nowhere near enough.

When he’d first picked up a sword, he’d wanted to become a great martial artist. After that, he’d wanted to become the pride of the Jin Family of Taiyuan—and a younger brother his elder brother could be proud of.

But there had been another reason, the greatest one, that he’d spent the past two years swinging his sword without rest in suffocating darkness.

He’d wanted to become a brother who could hold his head high.

He wanted to become strong enough to surpass the wall that was Cheongpung, so his younger brother, who’d become the Divine Dragon and soared freely through the sky, wouldn’t be ashamed of him.

But…

*So this is how it ends.*

Jin Mukyung, the Heaven Shaking Sword.

The time of opportunity granted to a young genius, overshadowed by other monsters, was over.

The sword he’d honed in the dark had shone brilliantly enough to light up this gorge today, but that fleeting ray would be swallowed by the long, deep night.

Forever.

*Damn it.*

Jin Mukyung struggled to lift his half-closed eyelids.

Refusing to close his eyes even in the face of death was his pride as a martial artist and proof that his fighting spirit remained unbroken. It was also his chance to say one last goodbye to his troublesome younger brother.

Even if his voice would reach no one.

“…I’m sorry.”

And just as the words were forced through Jin Mukyung’s lips—

*KABOOOOOM!*

The sky and earth shook.

Jin Mukyung’s world, dark and hazy until then, turned blue-white. The flash falling toward his head abruptly changed course, whipped aside.

Toward the terrible heat that came crashing in faster than light, faster even than the sound of the explosion.

No—to a spear carrying that terrible heat.

*Wooooom.*

The wind vanished. The air stopped.

The two currents of energy met for an instant, embracing the space around them for dozens of *zhang* before swelling enormously.

*KWAaaaa!*

A tremendous shock wave tore across the gorge, its roar deafening.

Lying in the deep pit, Jin Mukyung reached out on instinct.

He clutched the unconscious Cheol Mubaek and Wipeng with all his strength, and watched as the corpses of men and horses, along with countless chunks of rock, were swept up like leaves in a storm and hurled in every direction.

In the distant flash of light that engulfed everything around him, he also made out someone’s hazy back.

*Cough.*

Jin Mukyung spat up dark-red blood and suddenly wondered if he might already be dead.

Perhaps, unable to let go of his attachments from life, he was seeing things even after death.

But…

*No.*

It was vivid.

Everything he could see, hear, and feel in that moment was too real to believe it could be granted to the dead.

The stinging pain in his skin where the rock fragments had scraped past. The muscles screaming throughout his body. The blood surging from his insides, twisted by severe Internal Injury.

And, finally, the familiar voice that reached his ears.

“What are you throwing up for? Did you drink too much last night?”

Jin Mukyung’s body went rigid.

His eyes flew wide, a storm raging in their depths.

It was certain.

Not a hallucination. Not a trick of the ears.

This was…

“I’d pat you on the back, but, well, the situation’s a little tricky.”

The voice came through clearly, beyond the roar that was slowly dying away.

The figure stood out in the fading light.

That irritating voice alone was enough to make his fist clench.

The back of the wastrel, who had somehow grown broader and sturdier than his own.

“You…!”

Where had that strength come from?

Jin Mukyung squeezed out a voice rough as scraping metal and raised his hand.

His fingertips trembled like a leaf in a storm, his body already past its limit, as he reached for his only younger brother’s sleeve.

*Rustle.*

A tiny sound of friction, so faint he had to strain to hear it.

Perhaps it was the wind, not Jin Mukyung’s hand, that brushed the edge of his tattered robe.

But that was enough.

What he wanted to convey wasn’t just a touch. It was his desperate wish for his brother to protect everyone.

*Thud.*

His hand fell limply. His whole body went slack.

At last, after spending every last bit of his strength, the pathetic older brother lost consciousness.

Before him stood his wastrel younger brother, returned from two years away.

He faced an unfamiliar, graying middle-aged man who stood a dozen *zhang* away, staring straight at him with a somber gaze.

“I have one question.”

Flames poured from his eyes. His voice, by contrast, was cold as ice.

“Was it you who beat up my hyung?”

The wastrel had returned.

As a dragon whose roar shook the heavens.

Beyond his low voice, the people of Shanxi raised tearful cheers that rang out through the gorge.

* * *

A little while ago, someone had told me:

Don’t try to carry everything alone.

Try trusting them a little more.

And in that moment, I realized that person had been right.

I could tell as soon as I reached the battlefield.

Blood was everywhere. Severed limbs had fallen from bodies I couldn’t identify, and countless corpses of people and horses had piled up into small hills, filling the narrow gorge.

Most of them were nomads.

The enemy outnumbered us by at least two to one. But even with the odds stacked against them—not just in numbers, but in fighting strength—the people of Shanxi hadn’t given in.

No. They were squeezing out every last bit of strength to fight back.

The Imperial Army. The martial artists. Even ordinary people who hadn’t learned so much as a single move of martial arts.

And, finally, Jin Mukyung.

*They did everything they could. They even overcame their fear of death.*

I already knew how hard it was for the weak to stand against the strong.

And I’d taken Jin Mukyung’s wish to heart: there must be no more sacrifices like theirs.

*Wooooom. BOOM!*

I reached out, and a spear buried deep in the cliff twisted like a living creature and came flying toward me with a thunderous crash.

White Flame, back from its brief journey, trembled faintly in my grasp.

The blue-white flames coiling around its blade lit up the pitch-black darkness, heating the cold night air as they surged toward the enemy before me.

> **System**
> Lv.??? Murong Baek

The silver-haired, middle-aged man stood gripping a dark, ashen spear shaped much like the charging spears used by the nomads.

I’d be lying if I said the System window I read with my razor-sharp Qi Sense hadn’t caught me off guard. But the reality before my eyes was the truth.

I looked at him with a steady gaze—the Family Head of the Murong Family, whose name I’d heard but never met.

Another blade Dark Heaven had hidden in the vast forest of the Central Plains’ Murim: the North Heaven Demon Lord.

“I asked you. Was it you who beat up my hyung?”

The North Heaven Demon Lord was silent for a moment before he spoke.

“Well, this is a problem.”

His gaze swept over me. He let out a small sigh at the uninvited guest who’d shown up.

“A headache, in more ways than one.”

I bet it was. In more ways than one.

I raised my spear, ready to strike at any moment, and answered.

“Why the headache? You’re making me worry.”

It didn’t matter why or when the Family Head of the Murong Family had become Dark Heaven’s lackey.

I had only one thing to do: take down Murong Baek, without a doubt the North Heaven Demon Lord, and the nomad behind him, standing there with a thoroughly stiff expression.

“So why not just crack your skull while we’re at it? Then it won’t hurt anymore.”

*Step.*

The North Heaven Demon Lord took a step forward and replied calmly.

“That’s a treatment I’ve never heard of.”

“I know more about medicine than I look. I learned by watching the Divine Physician.”

“Maybe. Even so, I suspect that method would be a problem.”

The North Heaven Demon Lord looked at me with a clear gaze that seemed to see through everything, then added:

“Especially in your current condition.”

I wanted to deny it, but his judgment was accurate.

I’d paid a steep price to cross ten thousand *li* without proper sleep, meals, or time to circulate my qi.

So I answered without hesitation.

“Yeah, you’re right.”

*Step.*

The footsteps that had been steadily closing the distance suddenly stopped. The North Heaven Demon Lord furrowed his brow as he looked at me.

“What did you say?”

“I said you’re right. Honestly, as I am now, it’d be pretty tough. No, really tough.”

“What are you…”

His voice trailed off. I shrugged at the North Heaven Demon Lord, who was staring at me as if I were crazy.

“So I brought someone along. Figured I might as well.”

Before the North Heaven Demon Lord could understand what I meant, two cutting whistles swept through the air.
```
