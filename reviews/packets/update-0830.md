<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0830.txt",
      "sha256": "3167a7b984a63becc3290743ce8815db99fbd44018e60b849a2fd6a0a37c8674",
      "bytes": 12510
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "354466151c666284dcd75b4e0f295f7f1e1678d443b25acaf02c0707f0b92e17",
      "bytes": 2036
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3c3b9627e7353c69a66f8e10657ef055c79a30700111295e071d564e07f7e0ae",
      "bytes": 226707
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8e8f9b05638e3de665c6b1bb942afcac7c18ec158a63204b707511b77def8a3e",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "1b19489190c505d07bb0974d089a9eb5c0052a19894286c8dfc34400cc87f090",
      "bytes": 900
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ea5c61d0f8bf50184682f0d700b543f582991c7c51ad3e669aa4dc0033b2bc85",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "205d41aa03c973f4f63a068bc0fe084400bfe6e82970894a495e1d24ab26541a",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "21ea24cc51928413a96b86c8b4e996d0785e54dc7b9ded76e65166e79527e68b",
      "bytes": 251052
    }
  ],
  "estimated_tokens": 9391
}
-->

# Durable State Update — Chapter 830

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
1 and safe_through 830. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 830. Profile updates may replace only one
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
  "chapter": 830,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 830,
    "continuity_sources": [830],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Doppelganger known as The Prophet.",
    "The Doppelganger is the last surviving member of its species and can absorb appearances, abilities, and memories; it had Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger claims to have served Demon King Asmodeus and received his order to infiltrate humanity before Asmodeus fell.",
    "The Doppelganger says the temple’s empty throne was made for the Great King and that Asmodeus will return with his armies.",
    "Jin believes Asmodeus died on Victory Day, the day Jin was born, but cannot yet determine whether the Doppelganger’s claims are true.",
    "Jin’s white-blue flames destroyed the temple’s seventy-two Golems and magic circles, causing mana backlash in the Doppelganger.",
    "The Skeleton King interrupted the Doppelganger’s escape and repeatedly cut it down; it regenerated by consuming stored lives and remains as a Level 10 shadow after Jin’s attack.",
    "Jin’s Eye of Truth revealed the Doppelganger’s true essence as Level 10.",
    "Jin is confronting the Doppelganger over the devastation it caused; its claim that Asmodeus ordered its crimes has unsettled him."
  ],
  "continuity_sources": [
    828,
    829
  ],
  "open_questions": [
    "Is Demon King Asmodeus truly dead, and will he return?",
    "Are the Doppelganger’s claims about Asmodeus and the temple true?",
    "What caused the radiance that filled the temple?"
  ],
  "safe_through": 829,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword.”",
    "Render 에어 슬래시 as “Air Slash” and 실드 마법 as “Shield magic.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 성우 | **Sacred Rain** | Name later given to the rain released as the Earth Mother Goddess's blessing. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 실드 | **Shield** | Spell used by the Doppelganger to create layered barriers. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 829
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 829
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a Demon Realm being that can regenerate in new bodies by consuming its stored lives and is now reduced to a Level 10 shadow.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 829
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 829
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃830화



마계의 주인. 몬스터의 군주.

마왕 아스모데우스.

어찌 그 이름을 잊을 수 있을까. 모든 재앙의 시작점이자 근원 그 자체였던 악마의 존재를.

- 내, 내가 하고 싶어서 한 일이 아니다! 모두 왕께서 시킨 일이라는 사실을 잊었단 말이냐!

나는 다급하게 외치는 도플갱어를 말없이 내려다보았다. 그리고 짧은 갈등 끝에, 발끝을 향해 흘려보내던 공력을 회수했다.

- 쿨럭, 컥.

가슴에 가해지던 압박감이 해소됨과 동시에 터져 나오는 기침.

참았던 숨을 토해 낸 도플갱어가 분노와 고통이 뒤섞인 눈빛으로 나를 노려보았지만, 그 깊숙한 곳에는 미처 숨기지 못한 두려움이 웅크리고 있었다.

무려 170레벨에 달하던 네임드 몬스터라고는 믿기 어려울 정도로 무력한 모습.

그러나 지금 마주하고 있는 저 작은 그림자야말로, 도플갱어의 본질이자 유일한 진실이었다.

‘강력한 존재로 거듭나기까지, 지금껏 수많은 생명을 갈취해 왔겠지.’

닥치는 대로 뺏고, 흡수하고, 소화했을 것이다.

그들의 목숨을 양분 삼아, 계단 삼아 강자의 자리에 올랐을 것이다.

하지만 즐겁게 먹고 마시던 만찬의 시간도 오늘로 막을 내렸다.

도플갱어를 마치 신처럼 떠받들던 광신도들도, 몬스터 군단도 곁에 없는 지금. 놈의 앞에 놓인 길은 단 하나뿐이다.

“모조리 토해 내.”

꾸득.

잠시나마 사라졌던 천근(千斤)의 압력이 발끝에 실린다. 억눌린 신음을 토해 내는 도플갱어를 응시하며, 나는 나직이 말을 이었다.

“네가 알고 있는 게 뭔지. 그리고 무슨 일이 벌어지려고 하는지.”

마왕 아스모데우스.

악(惡), 그 자체이자 근원.

내가 도플갱어의 입을 통해 듣고자 하는 것은 바로 그 저주받은 존재에 대한 정보였고, 이 세상의 미래였다.

“조금 전에 했던 그 말.”

입술 사이로 흘러나온 갈라진 목소리가 남의 것처럼 낯설다.

마치 모래를 한 움큼 삼킨 것처럼 입안이 까끌거리는 것은, 비단 피로와 갈증 때문만은 아닐 것이다.

“놈이, 마왕이…….”

한 음절, 한 음절이 힘겹다. 감히 입에 담기도, 상상하기도 싫다.

그러나 나는 안다.

현실을 외면한 이들이 어떠한 말로를 맞이했는지. 그렇게 애써 외면한 현실 너머에 무엇이 도사리고 있는지.

산불을 피하기 위해서는 불의 존재를 인지해야 한다.

솟아오르는 연기와 붉은 화마(火魔)를 눈으로 확인하고, 타들어 갈 것 같은 열기를 느껴야 한다.

바로 지금처럼.

“아직, 살아 있나?”

숨 막히는 침묵 속, 머리 위로 작은 돌 부스러기가 쏟아져 내리는 소리만이 유난히도 크게 울려 퍼진다.

나도, 스켈레톤 킹도, 마지막으로 도플갱어도.

아주 잠시 동안은 그 누구도 입을 열지 않았다.

다음 순간, 인간의 것이 아닌 그림자의 속삭임이 들려오기 전까지는.

- 살아 있냐고?

스륵.

어둠이 일렁인다. 이목구비도 쉽게 구별할 수 없는 새까만 심연이 길게 찢어진다.

- 너는 모른다. 선택받은 자여. 동시에 언젠가는 세월에 꺾이고, 흙이 되어 스러질 어리석은 필멸자여.

도플갱어는 웃고 있었다.

나에 대한 분노도, 고통도, 두려움도 까맣게 잊어버린 채.

혹은 그 모든 것을, 이 자리에 없는 주인의 존재감으로 덮어 버린 채.

- 위대한 왕께서는 신의 저주를 극복하신 분. 흔들리되 꺾이지 않으며, 스러져도 일어나실 것이다. 그리하여 마침내 이 세상 모든 흙과 물을 당신의 것으로 만들 것이다.

“……!”

- 그것만이 진실이다. 알면서도 막을 수 없는, 머지않은 미래에 현실이 될 진실.

나는 멍하니 소리 내어 웃는 도플갱어를 바라보았다.

그리고 어둠이 소용돌이치는 그 눈을 마주한 그 순간, 눈앞이 아득해지는 것을 느꼈다.

‘이건.’

목소리가 새어 나오지 않는다. 사방에 자욱하던 모래 먼지와 돌무더기도, 스켈레톤 킹과 도플갱어도 사라졌다.

아니, 내 의식이 송두리째 어딘가로 빨려 들어가는 듯했다.

동시에 지금껏 본 적 없는, 환영과도 같은 광경이 마치 유성우처럼 눈앞으로 쏟아져 내렸다.

솨아아아악.

동쪽에서 떠오른 찬란한 태양이 세상을 물들인다. 푸른 하늘 위로 내달리는 구름. 이내 석양빛과 함께 달이 떠오르고 어둠이 찾아온다.

하루, 또 하루.

그것은 언젠가 봤던 자연 다큐멘터리 속 한 장면처럼 빠르게 흘러갔지만, 결코 아름답지 않았다.

콰아아앙!

굉음과 함께 거대한 불길이 솟구친다.

드넓은 자연 속에서 살아가던 야생동물들이 약속이라도 한 듯 일시에 내달린다. 석양과도 같은 화염을 등진 괴물들이 지평선을 메우며 진군했다.

드드드득.

수십, 수백만.

아니 어쩌면 그 이상.

감히 헤아릴 수도 없이 많은 몬스터의 대군세(大軍勢)가 사방에서 쏟아졌다. 지축을 뒤흔들고, 하늘을 뒤덮었다.

캬우우우!

구름 위에서부터 울려 퍼지는 끔찍한 포효.

거대한 날개가 구름을 훑고 햇빛을 가렸다. 그리고 어느 순간, 그것이 만든 그림자가 내 눈앞에 드리워졌다.

쉭.

시야가, 하늘과 땅이 뒤집힌다.

동시에 뒤바뀐 풍경 속에서, 나는 불타오르는 도시를 볼 수 있었다.

꽈아아앙!

수백여 개의 포신이 동시에 불을 뿜었다. 고층 빌딩과 키를 나란히 하는 거인들이 불길에 휩싸여 주춤하는 사이, 빛살처럼 쏘아진 신형들이 파괴된 거리를 가로질러 달려들었다.

광휘로 타오르는 무기를 들고, 피를 토하듯 자신들의 결의를 부르짖으며.

- 절대 물러서지 마라! 맞서 싸우라!

- 인류를 위하여!

그들은 헌터였다.

저주받은 존재들로부터 인류를 지키는 검과 방패.

보이지 않는 누군가의 선택으로, 거룩한 사명을 부여받은 전사들.

나는 손가락 하나 까딱하지 못한 채, 아득한 허공 위에서 그 장엄한 돌격을 지켜보았다.

그들은 수십 배가 넘는 몬스터들에 맞서 싸우고 있었다. 자신들의 외침을 증명하듯 결코 물러서지 않았고, 인류를 위해 피를 흩뿌리며 쓰러졌다.

해가 저물고 달이 떠오를 때까지.

그렇게 마지막 한 사람까지.

나는 이 모든 것을 그저 지켜볼 수밖에 없었다.

마치 누군가에 의해 조종당하듯이, 나이아가라 폭포가 피로 물들고 산산조각 난 피사의 사탑에 수백여 명이 압사(壓死)당하는 광경을 보았다.

나는 존재하지 않는 의식이었으며 관전자에 불과했다.

할 수 있는 것은 아무것도 없었다.

오직 쉴 틈 없이 뒤바뀌는 풍경 속에서 잿더미로 불타오르는 문명과 죽어 가는 사람들이 내지르는 비명을 보고 듣는 것이, 내게 주어진 단 하나의 권리이자 저주였다.

헤아릴 수 없는 죽음. 그리고 파괴.

거리가 시체로 뒤덮였다. 꺾여 나간 교회의 십자가가 피 웅덩이에 처박혔다.

부모가 어떻게 되었는지도 모른 채, 굶주림을 참지 못하고 작은 상자에서 빠져나온 아이 하나가 골목길에서 마주친 고블린 무리를 발견하고 손에 쥔 인형을 떨어트렸다.

재앙(災殃).

뜻하지 않은 불행한 변고를 뜻하는 말.

하지만 대격변을 상징하는 그 단어로도 감히 내가 본 끔찍한 광경들을 표현할 수는 없었다.

나는 나오지 않는 목소리 대신, 문득 한 단어를 떠올렸다.

‘종말(終末).’

그래, 그것은 종말이었다.

인류가 기나긴 세월 동안 쌓아 올린 문명은 파괴되었고, 사람들의 마음에는 한 줌의 희망조차 존재하지 않았다.

정확히 말하자면, 그들의 희망은 이미 죽었다.

한 사람씩. 천천히.

수백, 수천의 조각으로 나뉘어 굶주린 몬스터의 뱃속으로 사라졌다.

- 매직 존슨을 위하여.

수많은 촛불이 일렁이는 거대한 광장 위로, 나직한 목소리가 울려 퍼진다.

익숙하면서도 낯선 얼굴.

얼굴에 흉터가 가득하고, 한쪽 팔을 잃어버린 최 팀장이 술잔을 비운다.

샤오 쉔이 물기 어린 눈으로 술병을 들어 빈 잔을 채웠다.

- 일 년 전 오늘, 영원한 별이 되어 버린 ‘엉클 척’ 헤이글과 우리의 친구 스톤 킹을 위하여.

한 잔, 또 한 잔을 채우고 비울 때마다 연호되는 이름을 들으며 나는 깨달았다.

내가 바라보고 있는 이 광경은, 전사자들을 위한 추모식이라는 것을.

앞서 떠나간 영웅들을, 인류의 희망이었던 그들을 마지막으로 되새기는 출정식이라는 것을.

그리고.

- 누구보다 용맹했던 그를 위하여.

- 어둠에 맞서, 언제나 모두의 앞길을 밝혀 주었던 인류의 빛을 위하여.

내 모습이, 그 어디에도 보이지 않는다는 것을.

- 진태경을…… 위하여.

파르르 떨리던 목소리가 끝맺어진다. 몇 번째인지도 모를 술잔을 비운 최 팀장이 주먹을 쥐었다.

콰직.

산산이 부서진 잔의 파편과 함께 손아귀에서 흐른 핏물이 땅을 적신다. 촛불이 일시에 꺼지고 광장 전체가 침묵에 잠긴다.

동시에, 최 팀장의 허리춤에서 빛이 부풀어 올랐다.

화아아악.

영웅의 검.

깨지고 부서졌으나 여전히 날카로운 예기를 머금고 있는 검신 위로, 거대한 광휘가 샘솟았다.

촛불이 꺼진 광장 전체를 감싸안으며 짙은 어둠을 흐릿하게 밝혔다.

펄럭.

어느샌가 저 멀리에서 다가온 거센 바람이, 수십여 개의 크고 작은 깃발을 맹렬하게 흔들었다.

검과 방패가 교차된 문양. 조악한 그림으로나마 재현한 그것은 바로 세계 헌터 연맹의 깃발이었다.

- 물러설 곳은 없다.

쿵. 쿵쿵.

수천, 어쩌면 수만의 발끝이 지면을 굴렀다. 영웅의 검에 맺힌 광휘가 그들을 얼굴을 하나하나 비추었다.

- 물러서서도 안 된다.

캉! 카강!

허공에서 부딪친 날붙이가 불꽃을 토해 낸다. 탱커들이 커다란 타워 실드를 미친 듯이 내리찍고 두드렸다.

마치 거대한 심장이 맥동하는 것처럼, 그들은 하나의 뜻으로 움직이고 있었다.

먼저 떠나간 이들을 위해서, 그리고 앞서 벌어질 전투를 기다리며 자신들의 새로운 맹주를 바라보았다.

마지막 한 마디를 기다렸다.

- 우리는 오늘, 마지막 한 사람까지 싸운다.

차차차차창!

와아아아!

약속이라도 한 듯 동시에 솟구친 수많은 오러가, 하나의 목소리로 내지르는 아득한 고함이 어둠을 밀어낸다.

광장을 밝히던 촛불은 이미 꺼진 지 오래였지만, 인류의 불꽃은 아직 꺼지지 않았다.

적어도 오늘 이 자리에서 그들이 쓰러지기 전까지는 그러할 것이다.

마지막 불꽃을 잠재울 어둠이 다가오기 전까지는.

스아아아악!

그 순간.

바람이 멈췄다. 공기가 파르르 떨렸다.

한껏 열기가 달아올랐던 광장이 차갑게 식고, 수많은 눈동자가 한 방향을 향해 움직였다.

그리고 그곳에, 어둠을 두른 한 존재가 있었다.

- 아아…….

누군가의 입술 사이를 비집고 흘러나온 그 신음이, 내 귓가를 파고든다.

물에 잠겨 있는 것처럼 붕 떠 있던 감각이 되살아나고 전신의 털이 쭈뼛 섰다.

‘마왕.’

본능과도 같은 공포가, 경계심이 고개를 들었다. 나는 지금까지와는 달리 내 의지에 따라 고개를 움직였다. 모두가 바라보는 그 방향을 따라, 놈을 보았다.

마왕 아스모데우스.

과거에도, 아직 시작되지 않은 미래에도 인류를 불구덩이를 밀어 넣은 저주받은 왕을.

그리고 저 멀리 꿈틀거리는 어둠을 향해 눈을 부릅뜬 순간.

쩌저적.

나를 둘러싼 세계가, 모든 허상이 무너져 내렸다.
```

## Final English reading copy

```markdown
# Chapter 830

Master of the Demon Realm. Lord of the monsters.

Demon King Asmodeus.

How could I ever forget that name? The demonic being who was the starting point of every catastrophe, its very source.

“I-I didn’t do it because I wanted to! Have you forgotten that it was all on the king’s orders?”

I silently looked down at the Doppelganger, shouting in desperation. After a brief moment of hesitation, I drew back the internal energy I’d been channeling through my foot.

“Cough, hack.”

The pressure on its chest lifted, and it immediately broke into a fit of coughing.

The Doppelganger let out the breath it had been holding, then glared at me with eyes full of pain and fury. But deep inside them, fear lurked—fear it hadn’t quite managed to hide.

It looked so helpless that it was hard to believe it had once been a named monster at Level 170.

But the small shadow before me now was the Doppelganger’s true nature. Its one and only truth.

*It must have stolen countless lives to become so powerful.*

It had taken whatever it could, absorbed it, and digested it.

It had climbed to the heights of power on the backs of those lives, using them as food and stepping-stones.

But today, the feast it had so happily gorged itself on would come to an end.

Its fanatical followers, who’d worshiped it like a god, were gone. So was its army of monsters. With no one beside it, only one path remained.

“Spit it all out.”

*Crick.*

The crushing pressure I’d lifted a moment ago bore down through the tip of my foot once more. I watched the Doppelganger let out a muffled groan, then continued in a low voice.

“What you know. And what’s about to happen.”

Demon King Asmodeus.

Evil itself, and its source.

What I wanted from the Doppelganger was information about that accursed being—and the future of this world.

“What you said just now.”

The hoarse voice that slipped from my lips sounded like someone else’s.

My mouth felt as rough as if I’d swallowed a handful of sand. It wasn’t just exhaustion and thirst.

“He—the Demon King…”

Each syllable was a struggle. I didn’t dare say it aloud, or even imagine it.

But I knew.

I knew what became of those who turned away from reality, and what waited beyond the reality they’d tried so hard to ignore.

To escape a forest fire, you have to recognize that the fire is there.

You have to see the smoke billowing up and the red flames raging, and feel the heat that threatens to burn you alive.

Just as I was doing now.

“Is he still alive?”

In the suffocating silence, the sound of little bits of stone falling from overhead rang out with unusual clarity.

Neither I, nor the Skeleton King, nor the Doppelganger spoke.

Not for a brief moment.

Until I heard the whisper of a shadow, something not of this world.

“Is he still alive?”

*Stir.*

The darkness rippled. A pitch-black abyss, where its features were barely distinguishable, split into a long grin.

“You do not know, Chosen One. And yet you are also a foolish mortal, destined one day to be broken by time and crumble into dust.”

The Doppelganger was laughing.

It had forgotten its anger, pain, and fear of me.

Or perhaps it had covered them all with the presence of its absent master.

“Our Great King overcame the curse of the gods. He may waver, but he will not break. Even if he perishes, he will rise again. And at last, he will make all the earth and water in this world his own.”

“……!”

“That is the only truth. A truth you cannot stop, even knowing it—a truth that will become reality in the not-too-distant future.”

I stared blankly at the Doppelganger, laughing aloud.

And the moment I met its eyes, darkness swirling within them, I felt my vision grow hazy.

*This is…*

No sound came from my throat. The sand and rubble that had filled the area, the Skeleton King, the Doppelganger—they all vanished.

No. It felt as though my entire consciousness was being pulled somewhere.

At the same time, a vision unlike anything I’d ever seen came pouring into view like a meteor shower.

*SHWAAAAA…*

A brilliant sun rose in the east, bathing the world in light. Clouds raced across the blue sky. Before long, the moon rose with the glow of sunset, and darkness fell.

One day, then another.

It rushed by like a scene from a nature documentary I’d once watched, but there was nothing beautiful about it.

*BOOOOM!*

A tremendous blaze erupted with a thunderous roar.

The wild animals living in the vast wilderness bolted all at once, as if on cue. With flames like a setting sun at their backs, monsters marched across the horizon.

*Rumble…*

Hundreds of thousands. Millions.

Perhaps even more.

A horde of monsters beyond counting poured in from every direction. They shook the earth and blotted out the sky.

*Kyaaaaargh!*

A terrible roar rang out from above the clouds.

Huge wings swept across the clouds and blotted out the sunlight. Then, all at once, the shadow they cast fell over my eyes.

*Whoosh.*

My vision flipped. The sky and earth turned upside down.

And in the transformed landscape, I saw a city burning.

*BOOOOM!*

Hundreds of cannons fired at once. As giants standing shoulder to shoulder with skyscrapers staggered, engulfed in flames, figures shot forward like streaks of light and charged through the ruined streets.

They wielded weapons blazing with radiance and shouted their resolve as if spitting blood.

“Never retreat! Stand and fight!”

“For humanity!”

They were Hunters.

The sword and shield protecting humanity from the accursed beings.

Warriors given a sacred mission by someone unseen.

I couldn’t even twitch a finger. From high above, I watched their magnificent charge.

They fought monsters dozens of times their number. As if to prove their cries true, they never retreated. They fell, spraying their blood for humanity.

Until the sun went down and the moon rose.

Until the very last one.

All I could do was watch.

As if someone were controlling me, I saw Niagara Falls turn red with blood. I saw hundreds crushed to death beneath the shattered Leaning Tower of Pisa.

I was a consciousness that did not exist, nothing more than a spectator.

There was nothing I could do.

In a landscape changing without pause, the one right—and curse—granted to me was to see the civilization burning to ash and hear the screams of the dying.

Countless deaths. And destruction.

The streets were carpeted with corpses. A broken church cross lay plunged into a pool of blood.

A child, unaware of what had happened to their parents, could no longer bear the hunger and crawled out of a small box. When the child saw a pack of goblins in the alley, the doll in their hand fell to the ground.

Catastrophe.

A word for an unexpected, unfortunate disaster.

But even that word, a symbol of the Great Cataclysm, could not begin to describe the horrors I had seen.

In place of the voice that wouldn’t come, one word suddenly occurred to me.

*The end.*

Yes. It was the end.

The civilization humanity had built over countless years was destroyed, and not a glimmer of hope remained in people’s hearts.

To be exact, their hope was already dead.

One person at a time. Slowly.

Torn into hundreds or thousands of pieces, they disappeared into the bellies of hungry monsters.

“For Magic Johnson.”

A quiet voice rang out across a vast plaza flickering with countless candles.

A face both familiar and unfamiliar.

Team Leader Choi, his face covered in scars and one arm gone, drained his glass.

Xiao Shen lifted a bottle with tearful eyes and filled the empty glass.

“To ‘Uncle Chuck’ Hagel and our friend Stone King, who became eternal stars one year ago today.”

As I heard the names called out with every glass filled and drained, I understood.

This was a memorial for the fallen.

A send-off ceremony, a final remembrance of the heroes who had gone before us—the people who had been humanity’s hope.

And…

“To the bravest man of all.”

“To the light of humanity, who always illuminated the way for everyone as he stood against the darkness.”

My figure was nowhere to be seen.

“To Jin Taekyung…”

The trembling voice came to an end. Team Leader Choi drained yet another glass and clenched his fist.

*Crack.*

Blood ran from his hand, mingling with the shards of the shattered glass and dripping onto the ground. The candles went out all at once, and silence fell over the entire plaza.

At the same time, light swelled at Team Leader Choi’s waist.

*Fwoosh.*

The Hero’s Sword.

Though cracked and broken, its blade still held a keen edge. Brilliant radiance welled up from it.

The light embraced the entire plaza, where the candles had gone out, and faintly lit the deep darkness.

*Flap.*

A powerful wind, which had come from far away while no one was watching, whipped dozens of large and small flags.

A crossed sword and shield. Roughly depicted, but unmistakable: the emblem on the World Hunter Federation’s flag.

“There’s nowhere left to retreat.”

*Thud. Thud-thud.*

Thousands—perhaps tens of thousands—of feet stamped against the ground. The radiance gathered on the Hero’s Sword picked out their faces one by one.

“And we must not retreat.”

*Clang! Clang-clang!*

Blades clashed in the air, spitting sparks. The tanks slammed and pounded their massive tower shields like mad.

As if a giant heart were beating, they moved with a single purpose.

For those who had gone before them, and for the battle ahead, they looked to their new Alliance Leader.

They waited for his final words.

“Today, we fight until the very last person.”

*Chachachachang!*

“WAAAAH!”

Countless auras surged up at once, as if on cue. Their distant roar, raised as one voice, drove back the darkness.

The candles that had lit the plaza had long since gone out, but humanity’s flame still burned.

At least until they fell here today.

Until the darkness that would extinguish their final flame drew near.

*SHWAAAA…*

At that moment.

The wind stopped. The air trembled.

The plaza, heated to a fever pitch, turned cold. Countless eyes shifted in the same direction.

And there, stood a being cloaked in darkness.

“Ah…”

A moan slipped through someone’s lips and pierced my ears.

My senses, floating as if submerged in water, came back to me. The hairs all over my body stood on end.

*The Demon King.*

An instinctive fear and wariness stirred. Unlike before, I moved my head of my own free will. Following everyone’s gaze, I looked at him.

Demon King Asmodeus.

The accursed king who had once—and would again, in a future that had yet to begin—cast humanity into the flames.

And the moment I stared into the writhing darkness in the distance—

*Crack…*

The world around me collapsed. Every illusion shattered.
```
