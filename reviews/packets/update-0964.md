<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0964.txt",
      "sha256": "db6769d2753eec0317770b9e180e6a3e177351ffa3fe622f7a1034878c271464",
      "bytes": 14398
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "08b5b5da8aaaf560d3d7df032aebdaeca80203ec83ea5cb7ad61017ab52e4ac5",
      "bytes": 1962
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a9abc25b921cbdce05f090e91781cabe86a577757b8e253bfe7473b3c6a55ce2",
      "bytes": 235304
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "1f665d6b55ab158ce7360ffb373733c745f515a4155f21b18ac220ad031be0a2",
      "bytes": 1005
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f17febf0809868b6c353d25ed9ef84dcee90bd8b44d75e5b978408eb48e23965",
      "bytes": 759
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "7732a7d9c8eac7962487e8627f6517e6e65efe5677b44476e5392f6db38a9e25",
      "bytes": 1389
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "1c18899e575fe822a50aadf49183507eaa840a846035f50aed02ac6730c3be00",
      "bytes": 1095
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "6d00b076eb773e8222057fe9d9c12e1e037eb1268bb4907ca2b6f87b5719358c",
      "bytes": 1071
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "707d2a6be869228f3493f8630b695a6a5fceca518a03e31b47bf5171ff9f9540",
      "bytes": 911
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61539fa3c7a5bffe310bcd11125da2b97e0b99af8ca3198417d8586fa6465cf9",
      "bytes": 269140
    }
  ],
  "estimated_tokens": 11216
}
-->

# Durable State Update — Chapter 964

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
1 and safe_through 964. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 964. Profile updates may replace only one
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
  "chapter": 964,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 964,
    "continuity_sources": [964],
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
    "Jin Mukyung reached Supreme Peak and killed the Demon Bird, also known as the Blood Soul Fat Demon, at Eight Spring Gorge; he is severely injured but continues fighting.",
    "Cheol Mubaek and Wipeng are gravely wounded after helping Mukyung defeat the Demon Bird.",
    "Mukyung killed ten Keshik squad leaders with his newly named strike, Blue Wave, Falling Bird, and vowed to keep a promise.",
    "Jamukha has arrived and is facing Mukyung; a small but unmistakable tremor has begun.",
    "The Shanxi forces had regained momentum at Eight Spring Gorge; the horns sounded for Jamukha as the Keshik prepared to retreat.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    963,
    962
  ],
  "open_questions": [
    "What is causing the tremor, and how will the confrontation between Mukyung and Jamukha unfold?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Temur and the followers he led into battle?"
  ],
  "safe_through": 963,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 절정고수                | **Peak master** / **Peak martial artist** |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
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
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진무경 | 마조 | hostile opponents | you | blunt and insulting | Mukyung directly insults the Demon Bird, refusing to call him Master. |
| 마조 | 진무경 | hostile opponents | you | familiar and blunt, with admiration | Calls him a young Sword Demon and speaks to him with growing respect. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 963
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** His master, the Fist Hero, was a great fist master whose arms were severed by the Blood Soul Fat Demon; he is a close friend and peer of Lee Cheonbaek, a paternal uncle and protector of Lee Seowol, and considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 963
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 963
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 962
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he can agonize over costly decisions but commits firmly once resolved.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 949
- **Aliases:** None
- **Role:** Lee Seowol is the eighteen-year-old Sect Leader of the reconstructed and rapidly growing Mount Heng Sword Sect, a vassal of the Jin Family of Taiyuan who still awaits Taekyung’s answer to her marriage proposal.
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge, to whom he entrusted the Shura Annihilating Fist manual; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; during her farewell with Taekyung, she asked him to address her as Young Lady rather than Sect Leader.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 963
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung and a longtime sword mentor to Jin Mukyung, whom he taught as a boy. He remains alert to threats connected with Dark Heaven, and the Human Butcher has claimed him as a personal target.

## Korean source

```text
＃964화



드드득.

잔잔하게 고여 있던 피 웅덩이에 파문이 떠오른다.

자그마한 돌 부스러기도, 눈을 부릅뜬 채 죽음을 맞이한 수많은 시체들도 잘게 떨렸다.

‘이건.’

모두가 작지만 선명한 진동을 느꼈다.

그리고 동시에 직감할 수 있었다.

지진?

가당치도 않은 소리다.

이 진동은 최소 수천에 달하는 인마(人馬)가 이곳을 향해 가까워지고 있다는 결정적인 증거였다.

그 잔인한 징조는 누군가에게는 희망을, 또 다른 누군가에게는 깊은 절망을 안겨 주기에 충분했다.

와아아아아!

휘이이익!

협곡 안이 함성으로 가득 찼다.

마조의 죽음으로 인해 단번에 사기가 꺾여 있던 유목민들은 기성(奇聲)을 내지르며 달려들었다.

“지원군이다!”

“자무카 칸께서 오셨다!”

진무경이 마조를 쓰러트림으로써 전황(戰況)을 뒤집었다면, 이번에는 그 반대의 경우였다.

자무카.

산서인들로서는 이름조차 생소한, 서쪽 초원의 지배자이자 광활한 대초원의 절대자가 등장한 것으로도 모자라 최소 수천에 달하는 지원군이 합류한 상황.

조금씩 꺼져 가는 불씨처럼 연신 뒤로 밀려나던 유목민들의 사기는 하늘을 찌를 듯했고, 조금 전까지 침략자들을 몰아붙이던 산서인들은 잊고 있던 피로와 두려움을 느꼈다.

그들을 이끄는 한 사람 역시도.

‘이제는, 이제는 어떻게 해야 하지?’

진위경은 침음성을 삼켰다.

지금까지의 격전을 증명하는 것처럼, 총사령관인 그의 검에도 적들로부터 비롯된 핏물이 흐르고 있었다.

분명 최선을 다해 싸웠다.

직접 전투에 참여하여 아군의 사기를 북돋으며, 중간중간 몇 번의 위기가 있을 때마다 빈틈없는 지시로 협곡의 입구를 물 샐 틈 없이 틀어막았다.

산서성 전체에서 쥐어 짜낸, 만오천의 병력.

그러나 현실은 냉정했다.

만오천이나 되는 병력에서 주력이라 부를 수 있는 이들의 숫자는 총원의 절반에도 못 미쳤고, 그들마저도 끊임없이 밀려드는 적들을 상대로 싸우며 적지 않은 희생을 치러야 했다.

하나의 적을 쓰러트리면 둘이, 둘을 쓰러트리면 다섯이.

다섯을 쓰러트리면 열이 있다.

그리고 그 뒤에는, 여전히 수만의 적들이 기다리고 있다.

비좁은 협곡을 둘러싼 이 길고도 끔찍한 소모전에서, 결국 먼저 부서지는 것은 바위가 아닌 돌멩이다.

‘결국, 이렇게 될 수밖에 없었나?’

진위경은 거칠게 호흡하며 주위를 둘러보았다.

흐릿하고, 먹먹하다.

층층이 쌓인 시체를 타 넘어 서로에게 돌격한 적과 아군이 뒤얽히고, 못 박힌 듯 서 있던 그를 향한 가솔의 외침은 적들의 함성에 파묻혀 개울가의 징검다리처럼 뚝뚝 끊겨 있었다.

“……서, 어서!”

제대로 들을 수는 없었으나, 진위경은 가솔의 뜻을 고스란히 읽어 낼 수 있었다.

힘주어 옷소매를 당기는 손길.

절망과 다급함으로 가득한 표정.

이러한 반응을 보이는 것은 비단 눈앞의 가솔뿐만이 아니다.

주위의 모두가, 태원진가의 무인들은 물론 산하 문파의 장문인들과 관군들이 그를 향해 눈빛으로 말하고 있었다.

어서 물러나라고.

당신은 살아야 한다고.

‘그래, 그렇겠지.’

진위경은 저들의 마음을 충분히 이해했다.

승패의 저울추는 이미 기울었고, 초원의 침략자들은 생각했던 것 이상으로 강했다.

아니, 초원 깊숙이 심어진 암천의 저력이 너무나도 무시무시했다.

그러니 지금이라도 퇴각 명령을 내리는 것만이 상책이다.

최전선의 병력이 결사 항전하여 시간을 버는 동안, 총사령관인 자신은 남아 있는 병력을 수습하여 물러나는 것이야말로 최선의 방책이었다.

하지만…….

‘그 총사령관이, 꼭 나일 필요는 없겠지.’

희미하게 웃은 진위경은 느슨하게 풀려 있던 검 자루를 굳게 말아쥐었다.

지난 수년간 검보다 붓이 익숙했던 삶을 살아 온 그였으나, 한 사람의 절정 고수로서 지닌 검기(劍氣)는 조금도 무뎌지지 않았다.

서걱!

호위들을 뚫고 접근하던 케식 하나가 맥없이 쓰러진다.

군더더기 없는 솜씨로 적의 목을 베어 내며 나아가는 진위경의 모습에, 가솔이 황급히 재차 그의 뒤를 따랐다.

“소가주님, 어째서……!”

푸푹!

또 하나의 목숨을 취한 진위경이 입을 열었다.

“항산검문의 문주, 이소월에게 전하게. 지금 이 순간부터 그녀에게 모든 뒷일을 맡기겠다고.”

“……!”

“가게, 어서!”

진위경은 외침과 함께 힘차게 검을 흩뿌렸다.

전투에서 진 패장(敗將)이 돌아갈 곳은 없다. 수많은 아군의 목숨을 희생시킨 그가 남아야 할 곳은 바로 이곳이다.

‘영민한 그녀라면 잘 해낼 수 있겠지.’

무거운 마음의 짐을 덜어내니 검이 가볍다. 돌격창과 화살이 스쳐 지나가며 만들어 낸 상처에서 비롯된 고통에, 전신의 피가 뜨겁게 달아올랐다.

‘모두에게 약속했다. 이 땅을, 산서성을 지키겠노라고.’

동시에 다짐했었다.

모두가 겁에 질려 도망친다 해도 자신만큼은 이 자리에 남을 것이라고.

사는 것도, 죽는 것도 함께할 것이라고.

“오너라! 나, 진위경. 태원진가의 소가주가 여기 있다!”

콰드득!

맹수처럼 부르짖으며 나아가는 진위경의 모습에, 주춤하던 산서인들의 눈동자 깊숙한 곳에서 불길이 솟구쳤다.

어디서부터 시작되었는지 모를 전율이 정수리를 타고 전신을 관통한다.

저곳이다.

오랫동안 찾아왔던 한 사람이 바로 저곳에 있다.

이 척박한 땅과, 그 안에서 살아가는 이들을 누구보다 아끼고 사랑하는 이가.

진정한 산서성의 맹주(盟主)가.

“으아아아아!”

“소가주를, 산서성을 지켜라!”

협곡을 떨어 울리는 거대한 함성과 함께, 산서인들은 온 힘을 다해 돌격했다.

그들은 물러서지 않았다.

단 한 사람도.



* * *



진무경은 불현듯 전신에 스며드는 피로감을 느꼈다.

그것은 잠시나마 잊고 있었던 육신의 고통이자, 넘어설 수 없는 거대한 벽을 마주했을 때 느끼는 막연함이기도 했다.

‘결국, 이렇게 될 수밖에 없었던 겁니까?’

진무경은 하늘을 바라보며 마음속으로 뇌까렸다.

흐릿했던 달빛마저 먹구름에 잡아먹힌 하늘은 언제나 그래 왔듯이 아무런 대답도 들려 주지 않았다.

다만 이 또한 운명이라는 듯, 말없이 모두의 머리 위에 드리워진 채 지켜보고 있을 뿐이었다.

수많은 적과 아군을.

이승을 떠나 더는 살아 움직이지 못하는 시체들을.

그리고 그 중심에 우뚝 선 두 사람.

진무경과 자무카를.

“좋은 검이군. 신병이기(神兵利器)라 부르기에 조금도 부족함이 없을 정도로.”

자무카의 시선은 천천히 움직였다.

어둠 속에서도 새하얗게 빛나는 검신과 진무경, 마지막으로 피 웅덩이에 처박혀 미동조차 하지 않는 마조의 시체를 향해.

“놈은 늘 스스로를 사냥꾼이라고 칭했지. 살아온 세월이 무색할 만큼 오만하고, 멍청했어.”

담담한 눈빛과 말투.

마조의 죽음에 대해 조금의 아쉬움도 내비치지 않는 자무카의 모습에, 진무경은 검 자루를 쥔 손아귀에 힘을 더하며 입을 열었다.

“지금 그 말을 들었다면 슬퍼했겠군. 주인에게도 인정받지 못한 사냥개라는 소리니까.”

“주인?”

“제법 아끼던 수하였을 텐데. 아닌가?”

조금이라도 빈틈을 만들기 위해 던진 말이었지만, 그런 진무경을 바라보는 자무카의 눈빛은 일말의 흔들림조차 없었다.

“실망이군.”

“뭐?”

“차라리 세 치 혀 대신 그 검으로 말하게. 자네 같은 사람에게 격장지계(激將之計)는 어울리지 않아.”

“……!”

“아직 한참 어설퍼. 물론 그전에 상대를 잘못 고른 것도 크겠지. 저기 누워 있는 한심한 놈처럼.”

마조의 시체를 향한 그의 경멸 어린 시선에, 진무경은 입술을 깨물었다.

자무카의 말이 옳았다.

마조의 죽음을 이용해 상대방의 빈틈을 유도한 것은 처음부터 잘못된 판단이었다.

어째서인지 그 이유는 모르겠지만, 자무카는 가장 날카로운 송곳니를 지녔던 사냥개를 잃었음에도 아무런 심경의 변화가 없었다.

아니, 이해할 수 없게도 한편으로는 달가워하기까지 하는 듯했다.

‘뭐지? 도대체 어째서?’

진무경의 의문에 사로잡힌 그때, 흥미로운 눈빛으로 눈앞의 검귀를 바라보고 있던 자무카가 불현듯 입을 열었다.

“그 검, 휘두르지 않을 거라면 이만 내려놓는 것이 어떤가?”

순간, 자무카의 말뜻을 이해한 진무경은 자신도 모르게 실소를 터트렸다.

“항복하라는 건가, 다른 누구도 아닌 내게?”

“항복?”

미간을 찌푸린 자무카가 고개를 저었다.

“아니, 굴복하라는 뜻이지. 주인을 향해 배를 뒤집어 까고, 꼬리도 흔들고 발등도 핥는 개처럼.”

“……!”

“새로운 사냥개가 되어 줘야겠네. 다행히도 때마침 괜찮은 목줄이 하나 비었거든.”

진무경은 대답 대신 말없이 자무카를 응시했다.

그리고 불쑥 입을 열었다.

“혈혼비마, 아니 마조도 내게 비슷한 말을 했었지.”

“혹시 제자로 삼겠다던가?”

“돼지 울음소리라 귀 기울여 듣지는 않았지만, 비슷해.”

“놀랄 일도 아니로군. 그놈이라면 자네를 수련시켜서 언젠가는 직접 해치웠을 테니까. 물론 지금의 꼴을 보아하니, 그 상황이 되더라도 되려 자신이 죽었겠지만.”

담담하게 뇌까린 자무카가 말을 이었다.

“하지만 오해하지는 말아 줬으면 하네. 나는 마조와 달라.”

“아무리 봐도 더했으면 더했지, 덜한 놈처럼은 보이지 않는데.”

“사냥감이 아니라 사냥개로 키우려는 것뿐일세. 적절한 시기가 되면 목줄을 풀어 줄 수도 있고.”

“그래, 그러시겠지.”

스릉.

서늘하게 흩뿌려지는 예기(銳氣).

천천히 검을 곧추 세운 진무경은 새하얀 검신 너머로 말을 이었다.

“네놈이 말하는 그 적절한 시기가 됐을 때쯤이면, 내가 지키려는 모든 것이 사라져 있을 테고.”

이야기는 끝났다. 미련도 없다.

사냥개가 되어 살아남을 바에는 한 명의 인간으로, 태원진가의 이공자로 죽음을 맞이하는 것이 옳다.

이미 죽음을 각오한 진무경에게 있어, 자무카의 말은 처음부터 끝까지 모조리 개소리였다.

적어도 다음 순간 들려온, 자무카의 한마디를 듣기 전까지는.

“살려 주지. 자네는 물론 저들 모두를.”

“……뭐?”

“단지 지켜야 할 것이 있어 사냥개가 되기를 거부한다면, 내가 충분한 먹이를 주겠다는 뜻일세.”

눈을 부릅뜬 진무경을 응시하며, 자무카는 비명과 고함이 난무하는 전장을 가리켰다.

“혹시 알고 있나? 사냥개를 길들이는 방법은 의외로 간단하다는 것을.”

단순히 목줄을 채운다고 끝이 아니다.

완전히 길들여지지 않은 사냥개는, 목줄이 풀리는 순간 또 하나의 맹수가 되어 주인을 물어 버린다.

“하지만, 가장 굶주렸을 때라면 어떨까.”

단단한 목줄에 구속되어 며칠 밤낮을 굶은 사냥개는 온순해진다. 누군가를 깨물 힘도 남아 있지 않고, 난생처음 겪는 무력감에 자신이 짐승이라는 것을 깨닫는다.

“바로 그때일세. 주인이 나타나 먹이를 던져 주는 것은.”

슥.

자무카는 진무경을 향해 손을 내밀었다.

그 텅 빈 손바닥 위에는 아무것도 존재하지 않았으나, 진무경의 눈에는 똑똑히 보였다.

피가 뚝뚝 흐르는 고기 대신, 협곡 안에서 결사항전을 이어가는 수많은 산서인들의 모습이.

자신을 포함한 모두의 목숨이.

“……!”

진무경은 자신도 모르게 이를 악물었다.

눈앞의 상대를 향한 두려움 때문에?

틀렸다.

그건 희망이었다.

아주 잠시.

잠시 동안만 의(義)를 배신하고, 협(俠)을 외면하면 모두가 살아남을 수 있다는 희망.

이미 결말이 예정된 혈투를 계속해서 이어 나가는 저들을, 하나뿐인 형님과 자신의 등 뒤에서 죽음을 기다리는 두 절정고수를 살릴 수 있다는 희망.

“무경아!”

“안 된다! 절대!”

위팽과 철무백.

얼마 남지 않은 힘을 쥐어 짜내어 외치는 두 사람을, 진무경은 깊게 가라앉은 시선으로 응시했다.

“미안합니다. 두 분 모두.”

“……!”

“……!”

위팽과 철무백은 눈을 부릅떴고, 자무카는 미소지었다.

그리고 그런 자무카를 바라보며, 진무경은 입술을 뗐다.

“혹시 내가 말했던가?”

“말이라니. 무슨?”

“날 제자로 삼겠다는 어느 돼지 새끼한테, 뭐라고 대답해 줬었는지.”

조금 전보다 흐릿해진 미소를 띤 자무카를 향해, 진무경은 발걸음을 뗐다.

씹어 뱉는듯한 한 마디와 함께.

“개좆이나 빨아라.”

“……!”

자무카의 안색이 굳은 그 순간.

부우우우!

저 멀리, 수십여 개의 뿔피리가 동시에 토해 내는 울림이 협곡에 닿았다.

그리고 저 다급한 뿔피리 소리에 의미를, 자무카는 누구보다 잘 알고 있었다.

‘적습(敵襲)!’

동시에 깨달았다.

조금 전 협곡 안의 모두가 느꼈던 그 진동은, 유목민들만의 것이 아니었다는 것을.
```

## Final English reading copy

```markdown
# Chapter 964

*Rrrumble.*

Ripples spread across the pool of blood that had lain still.

Tiny fragments of stone trembled. So did the countless corpses, eyes wide open in death.

*This is…*

Everyone felt the tremor, small but unmistakable.

And at the same time, they knew instinctively what it meant.

An earthquake?

Ridiculous.

This tremor was undeniable proof that at least several thousand men and horses were closing in on them.

The cruel omen was enough to give some people hope, and others utter despair.

“Waaaaah!”

*Wheeeee!*

The gorge filled with shouts.

The nomads, whose morale had plummeted at the Demon Bird’s death, let out shrill cries and charged.

“Reinforcements!”

“Khan Jamukha has arrived!”

If Jin Mukyung’s defeat of the Demon Bird had turned the tide of battle, now the reverse was happening.

Jamukha.

A name unfamiliar even to the people of Shanxi. The ruler of the western grasslands, the undisputed master of the vast Great Steppe. And now, at least several thousand reinforcements had joined him.

The nomads’ morale, which had been sinking as steadily as a dying ember while they were pushed back, soared. The Shanxi defenders, who had been driving back the invaders moments ago, felt the fatigue and fear they had forgotten return to them.

Even the man leading them felt it.

*What do I do now? What am I supposed to do?*

Jin Wikyung swallowed a groan.

As if to prove how fierce the battle had been, blood from his enemies ran down his sword, the weapon of the commander in chief.

He had fought with everything he had.

He had joined the fighting himself to raise his men’s spirits. Whenever a crisis arose, he had given flawless orders, sealing the gorge entrance so thoroughly that not even a drop of water could pass.

Fifteen thousand troops, scraped together from across Shanxi Province.

But reality was cold.

Less than half of those fifteen thousand could be called the main force, and even they had suffered heavy losses fighting the enemies who kept pouring in.

For every enemy they felled, there were two. For every two, five.

For every five, ten.

And behind them, tens of thousands more still waited.

In this long, dreadful war of attrition around the narrow gorge, it was not the rocks that broke first, but the pebbles.

*Was this how it had to end?*

Jin Wikyung breathed hard and looked around.

Everything was hazy, muffled.

Enemies and allies charged at one another over heaps of corpses, all tangled together. His retainer’s cries to him as he stood rooted to the spot were drowned out by the enemy’s shouts, reaching him only in broken snatches, like stepping-stones across a stream.

“…urry, hurry!”

He couldn’t make out the words, but Jin Wikyung understood exactly what his retainer meant.

A hand tugging hard at his sleeve.

A face full of desperation and urgency.

And it wasn’t just the retainer in front of him. Everyone around him—the martial artists of the Jin Family of Taiyuan, the Sect Leaders of their vassal sects, and the government troops—was speaking to him with their eyes.

*You have to get out of here.*

*You have to live.*

*Yes. I suppose so.*

Jin Wikyung understood how they felt.

The scales of victory and defeat had already tipped, and the invaders from the steppe were stronger than anyone had expected.

No—the strength of Dark Heaven, planted deep in the steppe, was far more terrifying than he had imagined.

Even now, the best course was to order a retreat.

While the troops at the front held out to buy time, he—the commander in chief—could gather the remaining forces and withdraw. That was the best strategy.

But…

*There’s no reason the commander in chief has to be me.*

Jin Wikyung smiled faintly and closed his hand around the sword hilt he had been holding loosely.

He had spent the past few years more accustomed to a brush than a sword, but the Sword Energy of a Peak master had not dulled in the slightest.

*Shhk!*

A Keshik trying to break through his guards crumpled without a fight.

Jin Wikyung advanced, cutting down the enemy with clean, precise movements. His retainer hurried after him again.

“Lesser Family Head, why—”

*Thuk!*

Jin Wikyung took another life and spoke.

“Tell Lee Seowol, the Sect Leader of the Mount Heng Sword Sect, that from this moment on, I entrust everything that follows to her.”

“……!”

“Go. Now!”

With that shout, Jin Wikyung swept his sword through the air.

A defeated general had nowhere to return to. After sacrificing the lives of so many of his people, this was where he belonged.

*She’s clever. She’ll manage.*

With the weight on his heart lifted, his sword felt lighter. Pain flared from the wounds where lances and arrows had grazed him, setting his blood ablaze.

*I promised everyone. I would protect this land—Shanxi Province.*

He had made another vow, too.

Even if everyone else fled in terror, he would remain here.

He would live and die with them.

“Come on, then! I am Jin Wikyung, Lesser Family Head of the Jin Family of Taiyuan! I’m right here!”

*Crack!*

At the sight of Jin Wikyung advancing with a beast’s roar, a flame sprang up deep in the eyes of the Shanxi defenders who had been wavering.

A shiver, its origin unknown, raced from the crown of their heads through their entire bodies.

*There he is.*

The man they had been searching for all this time was right there.

The man who cherished and loved this barren land and the people living on it more than anyone.

The true Alliance Leader of Shanxi Province.

“Yaaaaah!”

“Protect the Lesser Family Head! Protect Shanxi Province!”

With a tremendous roar that shook the gorge, the people of Shanxi charged with all their strength.

They did not retreat.

Not one of them.

* * *

Jin Mukyung suddenly felt fatigue seep through his whole body.

It was the pain of his flesh, which he had momentarily forgotten, and the vague helplessness of facing an insurmountable wall.

*Was this how it had to end?*

Jin Mukyung looked up at the sky and muttered inwardly.

Even the faint moonlight had been swallowed by the clouds. As always, the sky offered no answer.

It simply hung over everyone in silence, watching, as though this too were fate.

The countless enemies and allies.

The corpses that had left this world and could no longer move.

And the two men standing tall at the center of it all.

Jin Mukyung and Jamukha.

“That’s a fine sword. More than worthy of being called a divine weapon.”

Jamukha’s gaze moved slowly.

To the blade, shining white even in the darkness. To Jin Mukyung. And, finally, to the Demon Bird’s corpse, sprawled in a pool of blood without so much as a twitch.

“He always called himself a hunter. Arrogant and stupid, considering how long he’d lived.”

His eyes and tone were calm.

Jamukha showed not the slightest regret at the Demon Bird’s death. Jin Mukyung tightened his grip on the hilt and spoke.

“If he’d heard that, he’d have been sad. You’re saying he was a hunting dog his master didn’t even acknowledge.”

“Master?”

“He was a subordinate you cared for, wasn’t he? Or was I wrong?”

Jin Mukyung had tossed out the remark to create even the smallest opening. But Jamukha’s gaze did not waver in the slightest.

“I’m disappointed.”

“What?”

“Speak with your sword, not that silver tongue of yours. A provocation like that doesn’t suit someone like you.”

“……!”

“You’re still far too clumsy. Though, of course, choosing the wrong opponent was a big part of it. Like that pathetic fool lying over there.”

At Jamukha’s scornful glance toward the Demon Bird’s corpse, Jin Mukyung bit his lip.

Jamukha was right.

Trying to provoke an opening by using the Demon Bird’s death had been the wrong move from the start.

Jin Mukyung didn’t know why, but even after losing his sharpest-toothed hunting dog, Jamukha seemed entirely unmoved.

No—somehow, he even seemed pleased.

*What is it? Why?*

As Jin Mukyung wrestled with the question, Jamukha, who had been studying the Sword Demon with interest, suddenly spoke.

“If you’re not going to swing that sword, why not put it down?”

For a moment, Jin Mukyung understood what he meant and let out a quiet laugh.

“You want me to surrender? To you, of all people?”

“Surrender?”

Jamukha frowned and shook his head.

“No. I mean submit. Roll over and show your belly to your master, wag your tail, and lick his feet like a dog.”

“……!”

“You’ll have to become my new hunting dog. Fortunately, I happen to have a spare collar.”

Jin Mukyung stared silently at Jamukha.

Then he spoke without warning.

“The Blood Soul Fat Demon—the Demon Bird—said something similar to me.”

“Did he offer to take you as his disciple?”

“I didn’t listen closely. It sounded like a pig squealing. But something like that.”

“That’s no surprise. He would’ve trained you and eventually tried to kill you himself. Though, looking at how he ended up, he’d have been the one to die.”

Jamukha spoke calmly, then continued.

“But don’t misunderstand me. I’m not like the Demon Bird.”

“You don’t look any better than him. If anything, you look worse.”

“I only intend to raise you as a hunting dog instead of prey. I might even let you off the leash when the time is right.”

“Sure. I bet you would.”

*Shing.*

A cold, sharp edge filled the air.

Jin Mukyung slowly raised his sword upright and spoke through its white blade.

“By the time that ‘right time’ you’re talking about comes, everything I want to protect will be gone.”

Their conversation was over. He had no regrets.

Better to die as a human being, the Second Young Master of the Jin Family of Taiyuan, than survive as a hunting dog.

To Jin Mukyung, who had already resolved to die, everything Jamukha had said was bullshit from beginning to end.

At least, until he heard Jamukha’s next words.

“I’ll spare your life. Yours, and all of theirs.”

“……What?”

“If you refuse to become a hunting dog because you have something to protect, then I mean to give you enough food.”

Jamukha looked at Jin Mukyung, whose eyes had widened, and gestured toward the battlefield, filled with screams and shouts.

“Do you know how to tame a hunting dog? It’s surprisingly simple.”

A leash alone was not enough.

A hunting dog that hadn’t been fully tamed would become a beast the moment its leash came off, and bite its master.

“But what if it’s starving?”

A hunting dog kept on a tight leash and starved for days on end would grow docile. It would have no strength left to bite anyone, and in the helplessness it had never experienced before, it would realize it was nothing but an animal.

“That’s when the master appears and tosses it some food.”

*Shk.*

Jamukha held out his hand toward Jin Mukyung.

There was nothing in his empty palm. Yet Jin Mukyung could see it clearly.

Not meat dripping with blood, but the countless people of Shanxi fighting to the death inside the gorge.

Everyone’s lives—including his own.

“……!”

Jin Mukyung gritted his teeth without realizing it.

Was it fear of the man in front of him?

Wrong.

It was hope.

Just for a little while.

The hope that if he betrayed righteousness and turned his back on chivalry for only a short time, everyone could survive.

That he could save the people continuing a blood-soaked battle whose ending was already decided, his one and only older brother, and the two Peak masters waiting to die behind him.

“Mukyung!”

“No! Absolutely not!”

Wipeng and Cheol Mubaek.

Jin Mukyung looked at the two men shouting with what little strength they had left, his gaze sunk deep.

“I’m sorry. Both of you.”

“……!”

“……!”

Wipeng and Cheol Mubaek’s eyes widened. Jamukha smiled.

Jin Mukyung looked at Jamukha and parted his lips.

“Did I ever tell you?”

“Tell me what?”

“What I said to a certain pig bastard who wanted to take me as his disciple.”

Jamukha’s smile had faded a little as Jin Mukyung stepped toward him.

With a single phrase, spat out through clenched teeth, he answered:

“Go suck a dick.”

“……!”

At the instant Jamukha’s expression hardened—

*Boooooo!*

Far away, the resonance of dozens of horns reached the gorge at once.

Jamukha knew better than anyone what that urgent blast meant.

*An enemy attack!*

And at the same time, he realized something.

The tremor everyone in the gorge had felt moments ago hadn’t belonged only to the nomads.
```
