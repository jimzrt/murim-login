<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0980.txt",
      "sha256": "2f1a363b582a7de94bea4590f1b7593890c6d92b9e413af1bb249d43e8e4f69d",
      "bytes": 12776
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d9fad904edea519824827f3926d52aae7f0c96c4119b56fc7210cc2a5029cf19",
      "bytes": 1151
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "534144353e21b1e77df6e1cab1ddd1ec71ab53581386f9d3c49a34452f7ba359",
      "bytes": 235946
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "26ce30071dee3af3970c407642870bb20f1e287ddb17893bf029b2a9c0009095",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "558eecb159c9bead47c522e90ad81b74ef7339e0728f9bf41991eea817d8d880",
      "bytes": 838
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "8aa1d5fd6cc6a862cebf535679abe4944823dd3932794076b79a423d8433d83c",
      "bytes": 1374
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "cfe41c04f695ebf842e08d50d134261621c5f3949243e043625d8dd805f35106",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4e87188c73c25bd52a6d12e9f6597de9b7367d0be3c22128f43294561af7ee1c",
      "bytes": 1442
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "72b0d9a52c66f2121e2ec65972b15461f692c3f85e248be2e14d1cd9eccceea1",
      "bytes": 271880
    }
  ],
  "estimated_tokens": 10237
}
-->

# Durable State Update — Chapter 980

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
1 and safe_through 980. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 980. Profile updates may replace only one
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
  "chapter": 980,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 980,
    "continuity_sources": [980],
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
    "Temur submitted to Jin Wikyung and the Jin Family of Taiyuan as his lord.",
    "The battle against the Murong Family resumed after the Jin Family’s reinforcements arrived.",
    "Jin Mukyung recalled his childhood and his father’s apology following his mother’s death in childbirth.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved.",
    "The conditions of Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown."
  ],
  "continuity_sources": [
    979
  ],
  "open_questions": [
    "What does the Lord of Heaven intend, and how will the war unfold?",
    "Who is the being in the darkness, and what is the day it has awaited?",
    "What are the conditions of Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?",
    "Who spoke to Jin Mukyung as he awoke?"
  ],
  "safe_through": 979,
  "temporary_decisions": [
    "Render Taekyung’s mocking nickname 뽀삐 as “Poppy”; it is not an established name."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 삼성     | **Three Saints**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 회음혈 | **Huiyin Acupoint** | Starting acupoint of the Conception Vessel; its location causes Taekyung particular danger during forced opening. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 979
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 977
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 943
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 979
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 979
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and their father—the Jin Family Head—once apologized to Mukyung for his mother’s death in childbirth.

## Korean source

```text
＃980화



눈을 동그랗게 뜬 진무경의 얼굴은 꽤 볼 만했다.

어쩌면 내 기억 속에 남아 있는 녀석의 태도와 모습이, 늘 딱딱하고 퉁명스러웠기 때문인지도 몰랐다.

“어, 깼냐?”

반가운 마음을 담아 건넨 인사.

분명 나를 바라보고 있음에도, 멍하니 풀려 있는 진무경의 눈동자에 맺힌 초점이 흔들렸다.

“아, 아버…….”

적지 않은 시간 동안 깨어나지 못해서일까.

잔뜩 쉰 목소리가 이어지지 못하고 흐려진다.

혼란스러워하는 기색이 역력한 녀석의 모습에, 옆에 있던 혁무진이 걱정스러운 얼굴로 입을 열었다.

“그, 혹시 머리에 문제라도 생기신 것 아닙니까?”

“이상하네. 약왕당주(藥王黨主)가 살펴본 바로는 크게 걱정할 필요 없다고 했었는데.”

“원숭이도 나무에서 떨어진다는데, 제아무리 약왕당주께서 산서성에서 난다긴다하는 명의(名醫)라고 해도 실수할 수 있죠. 나이도 있고.”

“쓰읍. 그런가?”

“사실 좀 쎄하긴 했습니다. 그 노친네, 환자가 치료 거부하면 대침으로 회음혈을 쑤셔 버린다고 협박하지 않습니까. 항산검문이랑 한창 치고받고 할 때 조장님께서도 당하신 거, 기억 안 나세요?”

당연히 기억난다.

팔뚝만 한 대침을 들고 강제 개통식을 열어 주겠다는 약왕당주의 모습은 공포 그 자체였으니까.

‘그래도 성질 머리와는 달리 실력은 확실했던 것 같은데.’

그뿐만 아니라 개인적으로도 여러 번 확인했다.

비록 공력을 주입하는 방식으로 상대의 내부를 관조하는 것에는 한계가 있다지만, 그런 사실을 감안하더라도 진무경의 상황은 그리 심각하지 않았다.

물론, 한 수 위의 초절정 고수를 상대로 격전을 치른 것 치고는.

“우선 약왕당주부터 모셔 와. 아, 그리고 혹시…….”

“가능하면 적 대협도 모셔 오겠습니다. 맞죠?”

“그래.”

눈치 빠른 놈 같으니.

이제는 척하면 착이다.

그리고 고개를 꾸벅 숙이고 돌아선 혁무진이 막 발걸음을 떼려던 그 순간이었다.

“여긴, 어디지?”

가뭄이 든 논밭처럼 갈라진 입술. 그 사이로 흘러나온 툭툭 끊어지는 음성.

하지만 아직은 안심하기 이르다.

이제야 조금씩 초점이 돌아온 진무경의 눈동자 위로, 나는 조심스럽게 손바닥을 흔들었다.

“이거 보여?”

“보인, 다. 그보다 여기는 어디…….”

“어디긴 어디야. 태원진가지.”

“그렇, 다면.”

무슨 말을 하려는지 충분히 짐작이 간다.

나는 어렵사리 목소리를 쥐어 짜내는 진무경을 위해, 그가 가장 궁금해하는 결과를 말해 주었다.

“이겼어.”

“아.”

“남아 있던 유목민들은 우리에게 완전히 굴복했고, 모용세가는 전원 죽거나 사로잡혔지.”

“다른, 다른 사람들은?”

꼬리에 꼬리를 물고 이어지는 물음을, 나는 못 들은 척하며 무시했다.

아직은 말할 수 없다.

아직은.

“나중에 말해 줄게.”

“뭐?”

“보아하니 아직도 눈빛이 맛이 갔구만, 뭘. 지금 내가 펼친 손가락 개수부터 말해.”

아직 정신이 완전히 되돌아오지 않았다는 건 진무경 스스로가 더욱 잘 안다.

은근슬쩍 화제를 돌리며 손가락 세 개를 펼치자, 찡그린 표정으로 나를 바라보던 진무경이 대답했다.

“셋.”

“좋아. 지금은?”

“다섯.”

척척 맞추는 걸 보니 이제 제법 정신이 돌아온 모양이다.

하지만 가장 중요한 마지막 절차가 남았다.

나는 비장한 얼굴로 신발을 벗어 발가락을 내밀었다.

“지금은?”

잠시 침묵하던 진무경이 입을 열었다.

조금 전과는 달리, 놀라울 만큼 단호한 음성으로.

“더러운 발 치워. 죽여 버리기 전에.”

“음. 완벽하군. 이제 좀 정신이 드십니까, 환자분.”

진무경이 얕은 한숨을 내쉬었다.

“그래, 이 개자식아.”

“어허, 개자식이라니. 친형제끼리 그런 말 하는 거 아냐. 누워서 침 뱉어 봤자 본인 얼굴에 떨어져.”

물론 실상은 피 한 방울도 안 섞인 이방인이지만, 이라는 말은 굳이 덧붙이지 않았다.

적어도 내가 지금 머무르고 있는 이 세상, 무림에서 태원진가의 삼형제는 같은 부모 아래에서 태어난 친혈육이었으니까.

하지만 내가 농담처럼 건넨 그 한 마디에, 찰나의 순간 진무경의 얼굴 위로 숨길 수 없는 묘한 감정의 소용돌이가 피어올랐다.

“뭐야, 왜 그래?”

“알 것 없다. 그냥…….”

잠시 망설이던 진무경이 말을 이었다.

“그냥 조금, 이상한 꿈을 꿨을 뿐이야.”

“이상한 꿈이라면, 악몽?”

“악몽까지는 아니지만……. 모르겠군. 말 그대로 이상한 꿈이었어.”

그렇게 말하는 진무경의 모습은 살짝 혼란스러워 보였지만, 나는 대수롭지 않게 어깨를 으쓱해 보였다.

‘뭐, 충분히 그럴 수 있지. 나만 해도 한번 기절할 때마다 별의별 꿈을 다 꾸는데.’

나로서는 익숙한 일이다.

아니, 많은 헌터들과 무림인들의 고질병 중 하나일지도 모른다.

사선(死線)을 넘나들다 보면 심리 상태가 변화하기 마련이고, 그처럼 불안정해진 심리는 종종 꿈속에서 드러나기 마련이니까.

“그래서, 몸 상태는 어때.”

“몸 상태라.”

섣부르게 침상에서 상반신을 일으켜 세우려던 진무경이 눈살을 찌푸렸다.

“뼈가 부러졌군. 당장 느껴지는 바로는 세 군데.”

나는 만족스럽게 고개를 끄덕였다.

환자 스스로 고통을 느끼고, 자신의 상태를 판단할 수 있다는 건 긍정적인 청신호다.

“정확하네. 약왕당주가 내린 소견과도 일치하고.”

“근육통이 심해서 움직일 수조차 없다. 누가 전신의 근육을 갈가리 찢어 놓은 느낌이야.”

“그렇게 무식하게 싸워 댔으니 아픈 게 당연하지. 매우 정상.”

“내상은……. 어째서인지 생각보다 심하지 않군.”

나는 기다렸다는 듯이 가슴을 쭉 폈다.

“그건 내가 힘 좀 썼지.”

“네가?”

“응. 고마워해도 돼.”

나를 물끄러미 바라보던 진무경이 고개를 끄덕였다.

“그렇군.”

“그게 다야?”

“그래.”

“음. 이상하네. 가정교육을 제대로 받은 사람이면 보통 이런 상황에서 고맙다고 하는데.”

“……불과 촌각 전에, 누워서 침 뱉기 운운하지 않았나?”

“내가? 언제?”

짐짓 어리둥절한 표정을 짓는 내 모습에, 작게 한숨을 내쉰 진무경이 입을 열었다.

“고맙다.”

“진심이 안 느껴져.”

“고맙다. 진심으로.”

“씁. 왠지 엎드려서 절 받는 기분인데.”

“…….”

“지금까지는 연습이라치고, 한 번 더. 이번에는 진짜로.”

크게 심호흡한 진무경이 대답했다.

“네 덕분에 살았다. 진심으로 고맙군.”

더 놀리고 싶었지만, 눈빛을 보니 이쯤에서 그만둬야 할 것 같다.

나는 아쉬운 마음을 감추며 진무경의 어깨를 툭툭 두드렸다.

“그래, 이제 좀 낫네. 지금 했던 감사 인사는 내가 잘 전해 줄게.”

“오랜만에 봐도 네 녀석은 정말 똑같……. 뭐? 전한다니, 그게 무슨 말이냐.”

“별거 아냐. 신경 안 써도 돼. 그냥 내상을 치료하는 과정에서 약간 도움을 준 사람들이 있어서.”

“도움? 누구에게?”

“있어. 화왕이랑 궁성이라고. 나름 좋으신 분들이야.”

“……?”

“아, 그러고 보니 일찍 기절해서 모르겠구나. 어쩌다 보니까 나랑 같이 오게 됐어.”

적천강이야 내가 태원진가에 머무를 때 본 적이 있으니 그렇다 치더라도, 궁성의 존재감은 아직 심신이 미약한 진무경에게 큰 충격을 선사한 것이 틀림없었다.

거칠어진 호흡을 가까스로 가다듬은 진무경이 목소리를 쥐어 짜냈다.

“궁성? 내가 아는 그 궁성?”

“어.”

“정마대전의 그 궁성? 활 쓰는?”

“아. 나도 그런 줄 알았는데, 그 활이 이리저리 만지다 보면 쌍도(雙刀)가 되더라. 약간 변신 로봇 느낌. 처음 보면 되게 신기해.”

“병신노복(病身老僕)……?”

“아니, 몸 불편한 늙은 하인 말고. 그, 변신 로봇이라고 있어. 물론 말해도 잘 알아듣지는 못하겠지만.”

그리고 내 짐작대로, 조금도 이해하지 못한 진무경은 짜게 식은 눈빛으로 나를 바라보고 있었다.

“도대체 그게 무슨 병신 같은 소리냐.”

“됐어. 그냥 넘어가.”

“그래, 그러는 게 좋겠군. 그러니까 결론은 네 녀석이 말하는 그 병신노복……. 아니, 궁성이 내가 알고 있는 그 삼성(三星) 중 한 분이 맞다는 거냐?”

슬슬 말이 꼬이기 시작하는 진무경을 향해, 나는 친절하게 고개를 끄덕여 주었다.

“정확해.”

“……도대체 어떻게 연이 닿은 거지?”

“황궁에서.”

“황궁?”

“어. 천하에서 모르는 사람이 없는 바로 그 황궁.”

“아니, 거긴 또 어떻게.”

“이게 좀, 말하자면 기니까 간단하게 알려 줄게.”

처음 의식을 회복했을 때보다 더 혼란스러워하는 진무경을 위해, 나는 명석한 두뇌로 빠르게 정리한 요약을 짧게 들려 주었다.

첫째. 황궁에 가서 황제를 만났다. 많이 무서운 동네였다.

둘째. 그곳에서 모두가 함께 으쌰으쌰 힘을 합쳐 동천마군을 쓰러트렸다.

셋째. 그 직후 산서성을 둘러싼 음모에 대해 알았다. 황제가 관직을 내리고 배웅까지 해 줬다.

“……그렇게 된 거야. 자, 이해됐지?”

그리고 내 간단명료한 정보 전달 과정을 지켜보던 혁무진이,작은 목소리로 중얼거렸다.

“제가 여섯 살 때 쓴 일기가 더 자세하겠는데요.”

짧은 이야기를 듣는 내내 멍한 표정을 짓고 있던 진무경도 뒤늦게 입을 열었다.

“진짜 미친놈인가.”

음.

천재의 사고방식을 이해하지 못하는 범인(凡人)들은 어디에나 있는 법이다.

어찌 되었건 최소한의 사정을 들은 진무경은, 그제야 모든 상황을 이해하고 고개를 끄덕였다.

“그러니까 결론은, 그 두 분이 내 내상을 치료해 주셨다는 거로군.”

“맞아. 확실히 이름값 하더라.”

“네놈은 한 것도 없으면서 감사 인사를 받았고.”

“한 게 없다니. 내 인맥이야. 일종의 대변인 자격으로 대신 감사를 받은 거지.”

“혹시 그거 알고 있냐?”

“아니, 나야 모르지. 아직 아무 말도 안 했으니까.”

“네 녀석이랑 대화하다 보면 종종 정신이 나갈 것 같아.”

“내가 좀 밝은 편이지. 일반인들은 감당하기 힘들 때가 있어.”

짐짓 밉살맞은 표정으로 씩 웃어 보인 그때, 진무경의 입가에도 씁쓸한 미소가 스쳤다.

“그것뿐이냐?”

“뭐?”

“단지 그것뿐이냐고 물었다. 평소보다도 훨씬 밝은 척 떠들고, 정신 산만하게 구는 이유가.”

나는 뒤통수를 긁적였다.

“글쎄. 뜬금없이 무슨 소리를 하는 건지 잘 모르겠는데.”

“이 년 전이 생각나는군. 오랜만에 본가로 돌아오니, 구제 불능이었던 망나니가 전혀 다른 사람이 되어 있었지.”

“…….”

“그런 갑작스러운 변화가 이상하긴 했지만 내심으로는 살짝 기뻤다. 완전히 새로운 사람으로 다시 태어난 것 같은 막내 녀석은, 겪어 볼수록 꽤 괜찮은 놈처럼 느껴졌거든.”

진무경이 덧붙였다.

“최소한 다른 수많은 이들의 죽음과 희생을 뒤로한 채 마냥 실없이 웃고 떠들 놈은 아니었지.”

그 순간, 나도 모르게 억지로 끌어 올린 입꼬리가 느슨해졌다.

그리고 더 이상 웃지 않는 나를 똑바로 응시하며, 진무경이 입을 열었다.

“더는 피할 수 없다는 것쯤은 너도 알 테니, 이제는 사실대로 대답해라.”

공기가 무겁게 가라앉는다. 흔들리는 진무경의 눈동자에 딱딱하게 굳은 내 얼굴이 비치고 있었다.

“도대체 누가, 얼마나 많은 이들이 희생당한 것이냐.”
```

## Final English reading copy

```markdown
# Chapter 980

Jin Mukyung’s eyes were wide open. It was quite a sight.

Maybe it was because the way I remembered him had always been so stiff and curt.

“Hey, you awake?”

I greeted him, glad to see him.

Though he was looking right at me, his dazed, unfocused eyes wavered.

“F-Father…”

Maybe it was because he’d been unconscious for so long.

His hoarse voice trailed off before he could finish.

Seeing how confused he looked, Hyuk Mujin, standing beside him, spoke up with worry written all over his face.

“Um, could there be something wrong with his head?”

“That’s strange. The Medicine King Hall Master examined him and said there wasn’t much to worry about.”

“Even monkeys fall from trees. No matter how famous the Medicine King Hall Master is as a physician in Shanxi Province, he can still make a mistake. He’s getting on in years, too.”

“Hmm. You think so?”

“To be honest, I had a bad feeling about him. Isn’t he the old geezer who threatens to ram a giant needle into a patient’s Huiyin Acupoint if they refuse treatment? Captain, don’t you remember when he pulled that on you while we were trading blows with the Mount Heng Sword Sect?”

Of course I remembered.

The Medicine King Hall Master had been terrifying when he’d announced he was going to perform a forced opening ceremony with a needle as thick as my forearm.

*Still, for all his temper, he seemed to know his stuff.*

I’d confirmed it myself several times, too.

There were limits to examining someone’s insides by channeling internal energy into them, but even taking that into account, Jin Mukyung’s condition wasn’t all that serious.

Of course, that was considering he’d just fought a Supreme Peak master who was a level above him.

“Go get the Medicine King Hall Master first. Oh, and if you can…”

“I’ll bring Great Hero Jeok too, if possible. Right?”

“Yeah.”

That kid was quick on the uptake.

Now he knew what I meant before I even finished saying it.

Hyuk Mujin gave a small bow and turned away. He’d just started to walk when—

“Where… am I?”

His lips were cracked like drought-stricken fields. His voice came out in broken, hoarse bursts.

But it was too soon to relax.

Jin Mukyung’s eyes were only just beginning to focus again, so I cautiously waved my palm in front of him.

“Can you see this?”

“I can… see it. But where is this…?”

“Where do you think? The Jin Family of Taiyuan.”

“If that’s… the case…”

I could guess what he was going to ask.

For Jin Mukyung, who was struggling to force the words out, I gave him the answer he wanted most.

“We won.”

“Ah.”

“The nomads who were left completely surrendered to us, and everyone in the Murong Family was either killed or captured.”

“What about… the others?”

His questions kept coming, one after another. I pretended not to hear and ignored them.

I couldn’t tell him yet.

Not yet.

“I’ll tell you later.”

“What?”

“Your eyes still look pretty out of it. Tell me how many fingers I’m holding up.”

Jin Mukyung knew better than anyone that he still wasn’t completely back to himself.

I changed the subject without making it obvious and held up three fingers. Jin Mukyung frowned at me, then answered.

“Three.”

“Good. And now?”

“Five.”

He was answering right away. Looked like his head was finally clearing.

But there was one last, most important step.

With a grave expression, I took off my shoe and stuck out my toes.

“And now?”

Jin Mukyung was quiet for a moment. Then he spoke.

Unlike before, his voice was astonishingly firm.

“Move your filthy foot before I kill you.”

“Hmm. Perfect. Feeling more like yourself now, patient?”

Jin Mukyung let out a shallow sigh.

“Yeah, you son of a bitch.”

“Now, now. You can’t talk like that to your own brother. Spit while lying down, and it’ll land on your own face.”

I didn’t bother adding *though in reality, I was an outsider with not a drop of their blood in me.*

At least in the world I was living in now—the Murim—the three sons of the Jin Family of Taiyuan had been born to the same parents.

But at that one teasing remark, an odd swirl of emotion surfaced on Jin Mukyung’s face for the briefest moment.

“What’s with you?”

“Nothing you need to know. It’s just…”

Jin Mukyung hesitated, then continued.

“I just had a strange dream.”

“A strange dream? A nightmare?”

“Not quite a nightmare… I don’t know. It was just strange.”

He looked a little confused as he said it, but I shrugged as if it were nothing.

*Well, it happens. I have all kinds of dreams every time I pass out.*

I was used to it.

No—maybe it was one of the chronic problems shared by Hunters and Murim people alike.

When you kept brushing up against death, your state of mind was bound to change. And an unsettled mind often revealed itself in dreams.

“So, how do you feel?”

“How do I feel…”

Jin Mukyung tried to sit up in bed too quickly and frowned.

“I’ve broken bones. Three, from what I can tell right now.”

I nodded, satisfied.

It was a good sign if the patient could feel the pain and judge his own condition.

“Exactly. That matches the Medicine King Hall Master’s diagnosis.”

“My muscles hurt so much I can’t even move. It feels like someone tore every muscle in my body to shreds.”

“Of course you’re in pain. You fought like an animal. That’s perfectly normal.”

“My internal injury… For some reason, it’s not as bad as I expected.”

I puffed out my chest, as if I’d been waiting for him to say that.

“I put in a little effort.”

“You did?”

“Yep. You can thank me.”

Jin Mukyung stared at me for a while, then nodded.

“I see.”

“That’s it?”

“Yeah.”

“Hmm. That’s strange. People who were raised right usually say thank you in a situation like this.”

“……Didn’t you just say something about spitting while lying down?”

“Me? When?”

I put on an innocent, confused expression. Jin Mukyung let out a small sigh.

“Thank you.”

“I don’t feel any sincerity.”

“Thank you. I mean it.”

“Hmm. Somehow it feels like I’m making you bow down and thank me.”

“……”

“Let’s say that one was practice. One more time. And mean it this time.”

Jin Mukyung took a deep breath before answering.

“I survived thanks to you. I’m truly grateful.”

I wanted to tease him some more, but from the look in his eyes, I figured I’d better stop here.

Hiding my disappointment, I patted his shoulder.

“Good. That’s more like it. I’ll make sure to pass along your thanks.”

“Even after all this time, you’re exactly the same… What? Pass them along? What do you mean?”

“It’s nothing. Don’t worry about it. There were some people who helped a little while treating your internal injury.”

“Helped? Who?”

“They’re here. The Fire King and the Bow Saint. They’re both pretty nice people.”

“……?”

“Oh, right. You passed out early, so you wouldn’t know. Somehow, they ended up coming with me.”

Jin Mukyung had seen Jeok Cheongang while I was staying with the Jin Family of Taiyuan, so that was one thing. But the Bow Saint’s presence must have come as a major shock to him, weak as he still was.

Jin Mukyung barely steadied his ragged breathing and forced out his words.

“The Bow Saint? The one I know?”

“Yeah.”

“The Bow Saint from the Great Faction War? The one who uses a bow?”

“Ah. I thought so too, but if you mess around with that bow enough, it turns into a pair of blades. Kind of like a transforming robot. It’s pretty cool the first time you see it.”

“A crippled old servant…?”

“No, not a disabled old servant. A transforming robot. Though you probably wouldn’t understand even if I explained it.”

Just as I’d expected, Jin Mukyung had no idea what I was talking about. He stared at me with a dead look in his eyes.

“What the hell are you talking about?”

“Forget it. Let’s move on.”

“Yeah, that’s probably for the best. So the crippled old servant you mentioned… No, the Bow Saint really is one of the Three Saints I know?”

I nodded kindly at Jin Mukyung, whose words were starting to trip over themselves.

“Exactly.”

“……How did you even meet them?”

“At the Imperial Palace.”

“The Imperial Palace?”

“Yeah. The very same Imperial Palace everyone in the land has heard of.”

“No, how did you even get there?”

“This is a bit of a long story, so I’ll give you the short version.”

For Jin Mukyung, who looked even more confused than when he’d first woken up, I gave him a quick summary, neatly organized by my brilliant mind.

First: I went to the Imperial Palace and met the Emperor. It was a pretty scary place.

Second: We all worked together to defeat the Eastern Heaven Demon Lord.

Third: Right afterward, I learned about the conspiracy surrounding Shanxi Province. The Emperor gave me an official post and even saw me off.

“……That’s what happened. Got it?”

Hyuk Mujin, who’d been listening to my concise and lucid explanation, muttered under his breath.

“My diary from when I was six was more detailed than that.”

Jin Mukyung, who’d been staring blankly the whole time, finally spoke up.

“Are you actually insane?”

Hmm.

There were ordinary people everywhere who couldn’t understand the thought process of a genius.

In any case, after hearing the bare minimum, Jin Mukyung finally understood the situation and nodded.

“So those two treated my internal injury.”

“Right. They lived up to their reputations.”

“And you got thanked even though you did nothing.”

“Nothing? They’re my connections. I accepted the thanks on their behalf, as their representative.”

“Do you know what?”

“No, how would I? I haven’t said anything yet.”

“Sometimes, talking to you makes me feel like I’m losing my mind.”

“I’m a pretty cheerful guy. Ordinary people can’t always handle it.”

I flashed him a deliberately obnoxious grin. A bitter smile touched Jin Mukyung’s lips too.

“Is that all?”

“What?”

“Is that really the only reason you’re pretending to be so much cheerier than usual, talking nonstop and acting so restless?”

I scratched the back of my head.

“Who knows? I’m not sure what you’re getting at.”

“It reminds me of two years ago. I came back to the family after a long time, and the hopeless good-for-nothing had become a completely different person.”

“……”

“The sudden change was strange, but deep down, I was a little happy. The youngest, who seemed to have been reborn as an entirely new person, turned out to be a pretty decent guy the more I got to know him.”

Jin Mukyung added,

“At the very least, he wasn’t someone who’d laugh and chatter thoughtlessly while leaving behind the deaths and sacrifices of so many people.”

At that moment, the corners of my mouth—which I’d forced upward—relaxed.

Jin Mukyung looked straight at me. I was no longer smiling.

“You know you can’t avoid this any longer, so answer me honestly.”

The air grew heavy. My stiff expression was reflected in Jin Mukyung’s wavering eyes.

“Who was it, and how many people were sacrificed?”
```
