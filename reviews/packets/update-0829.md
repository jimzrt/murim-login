<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0829.txt",
      "sha256": "9de524348556f74fc1c3a6d0d3069b2766a9cce41a0699ec3998a247a5c84f4b",
      "bytes": 13396
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e79b8b4d3e81cb8b3c3789986fc2dee9c6931b820099621bb9bf2f6aca284223",
      "bytes": 1980
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3c3b9627e7353c69a66f8e10657ef055c79a30700111295e071d564e07f7e0ae",
      "bytes": 226707
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "adf910c3c867b3e6b491778512ee521d57c6a9d097e4aa8c31c1ecdd8fdf5988",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "d2527ffabc5e28269862da55a47ea1f4d4e7318398d6e8297949d3579a5ac4c5",
      "bytes": 872
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "624b166b6e40550ef2666dd76b15bab1e4be10fbf6327083fcb4c9a9020857c7",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "011214f298fa9486a2657784b6a1cfc0f4c20c5316863c071e08921100352776",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "898fc299e6b8a76d354467b2f46a1b9d1555c54fe7c010a5fe6cee3036bf12e1",
      "bytes": 757
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "42d192e793607af11005fda62f61c712151134779e4d9f70ebd864a9f1edfc4e",
      "bytes": 250913
    }
  ],
  "estimated_tokens": 10062
}
-->

# Durable State Update — Chapter 829

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
1 and safe_through 829. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 829. Profile updates may replace only one
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
  "chapter": 829,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 829,
    "continuity_sources": [829],
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
    "The Doppelganger attempted to escape through a Teleport magic circle; the Skeleton King interrupted it and cleaved it in two, but its fate is unknown.",
    "Jin guided the temporarily blinded Skeleton King by Sound Transmission, helping him evade and counter the Doppelganger’s spells."
  ],
  "continuity_sources": [
    827,
    828
  ],
  "open_questions": [
    "Is Demon King Asmodeus truly dead, and will he return?",
    "Are the Doppelganger’s claims about Asmodeus and the temple true?",
    "Did the Doppelganger survive being cleaved in two?",
    "What caused the radiance that filled the temple?"
  ],
  "safe_through": 828,
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

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 삼류     | **Third Rate**    |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 일격     | **One Strike**                         |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 수마 | **sleep demon** | Metaphor for the force keeping Jin unconscious. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 레비아탄 | enemy and hunted monster | Leviathan; you | insulting-casual | Jin orders Leviathan to leave and dismisses its attempt to kill the Skeleton King. |
| 레비아탄 | 진태경 | attacking enemy | you bastard | enraged-insulting | Leviathan directly curses Jin while resisting his attacks. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 828
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 828
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 828
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 828
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 806
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus and withdrew into the deep sea after his fall; it regards the Skeleton King as a traitor for siding with humanity.

## Korean source

```text
＃829화



도플갱어.

수백여 년간 존재해 왔던 최후의 심연은 느리게 흘러가는 시간 속에서 모든 것을 보고 느꼈다.

쇄도하는 스켈레톤 킹.

거리를 벌리기 위한 블링크 마법.

그리고…….

슈확.

불현듯 귓가에 닿은 나직한 파공성과 함께, 시야를 가득 메운 황금빛 검광(劍光).

그 모든 것은 그야말로 찰나에 이루어졌고, 찰나에 끝났다.

마계의 가장 깊은 곳에서 탄생한 심연의 괴물이, 어떤 반응조차 할 수 없을 만큼 순식간에.

서걱.

뜨겁다.

막을 수도, 피할 수도 없었던 일격이 정수리를 가른다. 살과 뼈를 도려내고, 장기와 마나를 집어삼키며 사타구니까지 내달렸다.

마치 한 줄기의 벼락처럼.

‘아.’

도플갱어는 소리 없는 탄식과 함께 뒷걸음질 쳤다.

아니, 걸음을 떼었다고 느낀 순간 피 분수를 흩뿌리며 허물어졌다.

푸화아악!

선홍빛 핏물로 뒤덮인 시야가 천천히 기울어진다.

도플갱어가 갑작스럽게 찾아온 죽음을 인지함과 동시에, 지난 삼 년간 단단히 옭아매었던 영혼의 고리가 뜯겨 나갔다.

‘지크프리트 바스만.’

도플갱어는 똑똑히 느낄 수 있었다.

한때 영웅으로 칭송받던 대마도사의 마나가, 기억이, 아끼고 아껴 왔던 귀중한 생명력이 썰물처럼 빠져나가는 것을.

이 자리를 빠져나갈 수 있는 마지막 비행기의 티켓이, 지금 막 매진됐다는 것을.

철퍽.

정확히 두 갈래로 나뉜 몸뚱어리가 피 웅덩이에 처박혔다.

누구도 부정할 수 없는 죽음.

그리고 순리를 거스른 부활.

팟!

새로운 생명, 새로운 몸뚱어리에서 다시 태어난 도플갱어는 망설임 없이 몸을 날렸다.

텔레포트 마법으로 도주하는 것에는 실패했지만, 아직 활로는 남아 있었다.

‘최대한 멀리 떠난다. 남은 목숨을 모조리 바쳐서라도!’

지금껏 살아온 세월만 장장 수백 년이다.

그 기나긴 세월 동안 살아남기 위해 왕의 발치에 엎드렸고, 머지않아 도래할 그날에 확실한 보상을 약속받았다.

마계 72군단장? 오만하고 강대한 그들조차도 감히 자신과 같은 영광을 누릴 수는 없을 것이다.

아니, 어차피 그중 상당수는 이미 죽기까지 했다.

군단장 중 하나였던 레비아탄이 진태경에게 죽임을 당한 걸 알고 얼마나 비웃었던가.

그런데 그런 자신이, 위대한 왕의 오른편에 설 그가 이런 곳에서 개죽음당할 수는 없다.

‘살아남아야 한다. 나는 이곳에서 죽을 수 없어.’

도플갱어는 온 힘을 다해 뛰었다.

만일을 대비하여 숨겨 놓았던 신전의 출입구를 향해서.

머지않은 미래에서 자신을 기다리고 있을 무수한 영광을 향해서.

그리고 뒤늦게 깨달았다.

지금 이 순간, 살기 위해 달려가는 것은 자신의 하반신뿐이라는 것을.

서걱-

뒤늦게 울려 퍼진 절삭음이 귓가에 닿았다.

이미 잘려 나간 도플갱어의 상반신이 허공에서 기울어졌다.

몸이 분리된 것도 모르는 채, 처음의 힘 그대로 달려 나가는 하반신을 바라보는 주인의 눈동자에 아득함이 깃들었다.

“이런 개 같…….”

쉬쉬쉬쉭!

채 끝맺지 못한 한마디가 거센 파공성에 파묻힌다.

수십여 개의 육편(肉片)으로 화한 상반신이 허공에서 흩어짐과 동시에, 스켈레톤 킹의 검이 다시 한번 움직였다.

푹!

“끄읍.”

억눌린 비명.

조금 전의 처참한 죽음이 믿을 수 없을 만큼, 잘게 조각난 신체의 한 부위에서 새로운 몸뚱어리를 얻어 재탄생한 도플갱어가 몸부림쳤다.

가슴이 관통당한 상황에서도 붉게 핏발 선 눈동자는 오직 입구만을 향하고 있었다.

‘빌어먹을. 빌어먹으을!’

도플갱어는 들리지 않는 욕설을 내뱉으며 후회했다.

지난 삼십여 년간 인간들에게서 갈취한 영혼이 몇이던가. 또 그중 강자라 불리는 이들은 얼마나 많았던가.

모른다. 도플갱어 자신조차도 헤아릴 수 없었다.

그 모든 것은 단지 일종의 수확에 가까웠다. 양계장의 주인이 매일 아침 암탉이 낳은 알들을 거두어들이는 것처럼, 도플갱어는 인간들의 영혼을 모았고 그중 대부분을 거리낌 없이 소모했다.

상관없었다.

아무리 줄어들어도 채워 넣으면 그만이었고, 채우지 않아도 충분했다.

아니, 충분했었다.

적어도 오늘, 인간의 탈을 뒤집어쓴 괴물을 만나기 전까지는.

슁.

서늘한 바람이 목덜미를 스친다. 예리한 칼날이 가르고 지나간 목의 단면에서 죽음과 탄생이 동시에 찾아온다.

아니, 도돌이표처럼 끝없이 반복되었다.

서걱! 푹! 쉬쉬쉭!

베이고, 찔리고, 수십 조각으로 분해되어 흩어진다.

그럴 때마다 도플갱어는 사내, 여인, 노인의 모습으로 죽고 되살아났다. 그들에게서 빼앗은 힘과 기억을 바탕으로 입구를 향해 가까워졌다.

백여 미터의 거리가 수십여 미터로.

수십여 미터의 거리가 수 미터로 좁혀질 때까지.

이제는 단순한 소모품이 아니게 된, 하나하나가 귀중해진 목숨을 내던지며.

‘더 이상은…… 더 이상은 잃어선 안 된다.’

소멸(掃滅)이라는 단어와 함께 공포가 고개를 든다.

일천을 헤아리던 수많은 생명은 어디에도 없다.

이제는 두 손으로 헤아릴 수 있을 만큼 바닥을 드러내고 있는 생명력을 느끼며, 도플갱어는 혼신의 힘을 다해 또 다시 일어났다.

스륵. 쏴아악!

마치 옛 동화 속에 등장하는 콩 나무처럼 순식간에 재생된 신체. 말로는 설명할 수 없는 기괴한 탄생과 함께, 도플갱어는 황급히 몸을 굴렸다.

촤악!

불에 덴 듯한 통증이 등줄기를 훑는다.

하지만 고통의 잔재보다 살아남고자 하는 욕망이 더욱 컸다. 목숨을 도외시하고 몸을 날리는 도플갱어의 모습에, 스켈레톤 킹이 망설임 없이 손을 뻗었다.

푸푸푹!

순간 비틀거리는 신형.

도플갱어는 울컥 솟구치는 핏물을 삼켰다.

가슴 한복판에 비죽 솟아 있는 새하얀 무언가가 보였다. 동시에 종아리를 관통해 지면 깊숙이 틀어박힌 또 다른 뼛조각도.

“어딜 도망가려고.”

깊게 가라앉은 목소리와 함께 등 뒤로 불어닥치는 바람.

순식간에 가까워지는 스켈레톤 킹의 기척을 느낀 도플갱어가 이를 악물었다. 종아리와 지면을 꿰뚫은 뼛조각은 말뚝처럼 견고했다.

으득!

스켈레톤 킹에 비하면 한참이나 떨어진다고는 해도, 새로운 육신 역시 A급 헌터라고 부르기에 손색이 없는 수준.

스스로 무릎 아래를 뜯어낸 도플갱어는 하나밖에 남지 않은 외다리를 움직였다.

온 힘을 끌어 올려 지면을 박찼다.

쾅!

굉음과 함께 거센 바람이 전신을 스친다.

어느덧 코앞까지 가까워진 신전의 입구를 바라보는 도플갱어의 눈동자가 열망으로 들끓었다.

이곳만. 이곳만 빠져나간다면.

어떻게든 소멸을 피할 수만 있다면…….

‘맹세코, 너희가 지키고자 했던 이 세상을 잿더미로 만들어 버릴 것이다.’

그리고 오직 그에게만 허락된 비밀의 문을 향해 손을 내뻗은 순간.

쐐애애애액.

저 멀리 어디선가.

콰직!

공간을 가르며 날아든 섬광이 도플갱어의 전신을 집어삼켰다. 산산이 찢고 부수었다.

까맣게 물든 시야 속에서 한 사람의 목소리가 도플갱어의 귓가를 파고들었다.

“이 씨벌 새끼가, 손님 불러 놓고 어딜 가.”

그 음성이 어찌나 서늘하던지.

반면 몸 안을 파고든 창날에서 터져 나온 불길은 어찌나 뜨겁던지.

화륵.

콰아아아!

온통 푸르고 희게 물든 시야 속, 청백색의 화염에 휩싸인 도플갱어는 비명조차 내지르지 못하고 몸부림쳤다.

한때 다른 누군가의 것이었던 육신이, 생명력이 모조리 재가 되어 타들어 갈 때까지.

그리고 지금껏 쌓아 왔던 모든 거짓이 불타오른 그 자리에, 단 하나의 진실이 남을 때까지.

저벅, 저벅.

솨아아아.

비틀비틀 나아가는 발걸음을 따라 불어온 바람이 잿가루가 흩날린다.

소복하게 쌓여 있던 그것의 틈바구니에서 검고 희뿌연 그림자가 꿈틀거렸다.

“……그래.”

스켈레톤 킹의 부축을 받아 앞에 선 진태경은 은은한 빛이 어린 눈으로 그림자를 내려다보았다.

온통 거짓으로 점철된 존재의 유일한 진실. 그 하찮은 본질을 꿰뚫었다.



[Lv.10 도플갱어]



“고작 이 정도였구나. 너는.”

- ……!

그림자가, 아니 도플갱어가 몸을 떨었다.



* * *



단지 서 있는 것뿐인데도, 그뿐인데도 호흡이 가쁘다.

서서히 멀어지는 감각과 흐릿한 시야 속에서는 가파르게 뛰는 심장박동 소리가 천둥처럼 울려 퍼진다.

쿵. 쿵쿵.

마지막 일격에 모든 힘을 쏟아부은 대가일까.

전신이 파르르 떨렸다. 만약 스켈레톤 킹이 나를 부축하지 않았다면 진작 쓰러지고도 남았을 것이다.

하지만 나는 쓰러지지 않았다.

지금 이 순간에도 사방에서 쏟아져 들어오는 수마(睡魔)을 밀어내고, 스켈레톤 킹의 부축마저 풀어 내며 두 다리로 우뚝 섰다.

그리고 굽어보았다.

어린아이처럼 작고, 어린아이와는 비교도 되지 않을 만큼 순수한 악(惡)으로 이루어진 그림자를.

이제 한낱 그림자에 지나지 않게 된 끔찍한 존재를.

“그래, 고작 이 정도였어.”

앞서 했던 말을 혼잣말처럼 뇌까린다.

겁먹은 듯 부르르 몸을 떠는 도플갱어의 모습을 보자, 놈의 머리 위에 떠올라 있는 레벨 창을 보자 나도 모르게 헛웃음이 흘러나올 것만 같았다.



[Lv.10 도플갱어]



레벨 10.

그게 전부다. 더할 것도, 뺄 것도 없다.

헌터로 치면 F급 중에서도 밑바닥이고, 무림인으로 치면 이제 막 공력을 겨우 느끼기 시작한 삼류 칼잡이 수준.

그것이 [진실의 눈]으로 확인한 도플갱어의 본질이었다. 근원이며 오직 하나뿐인 진실이었다.

‘겨우 이런 놈한테.’

차오르는 말을 삼키며 이를 악물었다.

눈을 감자 드리워진 어둠 속에서는 불길이 일렁이고 있었다.

처참하게 파괴당한 도시.

곳곳에서 솟구친 연기 사이로 널브러진 시체들이 보인다. 아직 살아 있는 이들이 내지르는 비명이 귓가에 울려 퍼진다.

도플갱어가 벌인 테러로, 몬스터들로 인하여 도대체 몇 명이 죽었나.

얼마나 많은 이들이 터전을 잃고, 소중한 가족과 친구를 떠나보내야 했나.

수십만? 수백만?

모른다.

도플갱어가 세상에 스며든 지 어언 삼십여 년이 넘는 세월이 지났으니, 놈이 장막 뒤에서 어떤 일을 벌였는지 짐작조차 할 수 없다.

까드드득.

한껏 힘이 들어간 두 주먹.

손톱이 깊게 파고든 살갗 사이로 붉은 핏방울이 흐르는 것을 느끼며 눈을 떴지만, 어느 것 하나 사라지지 않았다.

폐허가 된 도시도. 죽은 이의 눈에 깃든 공허함과 살아 있는 이들의 울부짖음도.

그 모든 것을 머리가 기억한다. 지워지지 않는 낙인처럼 눈과 귀에 새겨졌다.

그리고 그중 유일하게 내 눈앞에 있는 것은, 단 하나뿐이다.

콰득.

- 컥. 커허헉.

공력이 실린 발끝이 그림자를 짓누른다.

이런 저주받은 형태로도 고통을 느끼는지, 억눌린 신음과 함께 몸부림치던 도플갱어가 애원했다.

- 사, 살려…….

“살려 달라고?”

- 그래, 뭐든. 뭐든 할 테니까! 그럴 테니까!

문득 멍해진 나는 놈을 물끄러미 내려다보았다. 그리고 남아 있는 공력을 끌어모아, 발끝을 향해 거세게 흘려보냈다.

우득. 우드득!

- 끄아아아!

비명을 내지르는 도플갱어의 모습을 그저 지켜만 보고 있던 그때.

스켈레톤 킹이 불현듯 내 어깨에 손을 올렸다.

“인간.”

“왜?”

그저 반문했을 뿐인데, 내 얼굴을 마주한 스켈레톤 킹이 조용히 입술을 달싹였다.

“……아니다.”

지금 이 순간 나는 어떤 얼굴을 하고 있을까. 지치고 힘들어하고 있을까. 아니면 지금껏 본 적 없는 분노로 일그러져 있을까.

아마도 후자였을 것이다.

고통에 몸부림치던 도플갱어가 내 표정을 보고 비명을 멈췄으니까.

공포에 질린 목소리로 이렇게 말했으니까.

- 내, 내가 하고 싶어서 한 일이 아니다! 모두 왕께서 시킨 일이라는 사실을 잊었단 말이냐!

왕.

마왕 아스모데우스.

놈의 외침과 함께 떠오른 그 존재의 이름에, 몸과 마음을 사로잡고 있던 분노가 흔들렸다.
```

## Final English reading copy

```markdown
# Chapter 829

The Doppelganger.

The last abyss, which had existed for hundreds of years, saw and felt everything in the slow passage of time.

The Skeleton King charging toward it.

Blink magic to put some distance between them.

And…

*SHWAK.*

Along with a soft rush of air that suddenly reached its ears, a golden flash of swordlight filled its vision.

It all happened in the blink of an eye—and ended in the blink of an eye.

The monster of the abyss, born in the deepest reaches of the Demon Realm, couldn’t react at all. It happened that fast.

*Slice.*

Hot.

The strike it could neither block nor dodge split its crown. It carved through flesh and bone, devoured its organs and mana, and raced down to its crotch.

Like a bolt of lightning.

*Ah.*

The Doppelganger staggered backward with a silent sigh.

No—at the moment it felt itself take a step, it crumpled, spraying a fountain of blood.

*SPURT!*

Its blood-red view tilted slowly.

As the Doppelganger recognized the sudden arrival of death, the chain around its soul—wound tight for the past three years—was torn away.

*Siegfried Bassman.*

The Doppelganger could feel it clearly.

The mana, memories, and carefully hoarded vitality of the Grand Mage once hailed as a hero were draining away like the tide.

The ticket for the last flight out of here had just sold out.

*Splash.*

The body, split cleanly in two, crashed into a pool of blood.

A death no one could deny.

And a resurrection that defied the natural order.

*Pop!*

Reborn in a new life, in a new body, the Doppelganger threw itself forward without hesitation.

It had failed to escape using Teleport magic, but there was still a way out.

*I’ll get as far away as possible. Even if I have to spend every life I have left!*

It had lived for hundreds of years.

Throughout that long life, it had survived by prostrating itself at the king’s feet—and had been promised certain rewards on the day that would soon arrive.

A commander of one of the Demon Realm’s seventy-two legions? Even those arrogant, mighty beings couldn’t dare dream of sharing a glory like its own.

No, many of them had already died anyway.

It had laughed so hard when it learned that Leviathan, one of the commanders, had been killed by Jin Taekyung.

But it couldn’t die like this. Not when it was destined to stand at the Great King’s right hand.

*I have to survive. I can’t die here.*

The Doppelganger ran with all its strength.

Toward an exit from the temple it had hidden away in case of emergency.

Toward the countless glories waiting for it in the near future.

And only then did it realize.

At this very moment, only its lower half was running to save its life.

*Slice—*

The delayed sound of something being cut reached its ears.

The Doppelganger’s upper half, already severed, tilted in midair.

Its eyes, looking down at the lower half as it ran on with its original strength, held a distant, dazed look. It didn’t even know its body had been split apart.

“You son of a—”

*SH-SH-SH-SH!*

The forceful rush of air swallowed the unfinished words.

As the upper half burst into dozens of pieces and scattered through the air, the Skeleton King’s sword moved once more.

*Thrust!*

“Ghk.”

A suppressed groan.

In one small piece of its body, the Doppelganger gained a new body and was reborn, as if the gruesome death moments ago had never happened. It writhed.

Even with its chest pierced, its bloodshot eyes were fixed solely on the exit.

*Damn it. Damn it!*

The Doppelganger cursed soundlessly, regretting everything.

How many souls had it stolen from humans over the past thirty years? And how many of them had been people called strong?

It didn’t know. Even the Doppelganger itself couldn’t count them all.

It had all been little more than a harvest. Like a chicken farmer gathering the eggs his hens laid each morning, the Doppelganger collected human souls, and spent most of them without a second thought.

It didn’t matter.

No matter how much it used up, it could simply replenish them. Even without replenishing them, it had more than enough.

No—it had had more than enough.

At least, until today, when it met a monster wearing a human’s skin.

*Swish.*

A cold breeze brushed its nape. As a razor-sharp blade sliced through its neck, death and rebirth arrived together.

No—they repeated endlessly, like a broken record.

*Slice! Thrust! SH-SH-SH!*

It was cut, stabbed, and broken into dozens of pieces that scattered through the air.

Each time, the Doppelganger died and came back in the form of a man, a woman, or an old person. It drew on the powers and memories it had stolen from them as it edged closer to the exit.

A hundred meters narrowed to dozens.

Dozens of meters narrowed to a few.

It threw away its lives one by one, each now precious rather than a mere expendable resource.

*I can’t… I can’t lose any more.*

Fear rose at the word *Erasure*.

The lives that had once numbered around a thousand were nowhere to be found.

Feeling its vitality dwindle until it could count what remained on both hands, the Doppelganger summoned every ounce of strength and stood up again.

*Slide. WHOOSH!*

Its body regenerated in an instant, like a beanstalk shooting up in an old fairy tale. With a grotesque rebirth that words couldn’t explain, the Doppelganger hurriedly rolled away.

*Slash!*

A pain like a burn raked down its back.

But its desire to survive was stronger than the pain that lingered. As the Doppelganger threw itself forward, heedless of its life, the Skeleton King reached out without hesitation.

*Thud-thud-thud!*

Its body staggered.

The Doppelganger swallowed a surge of blood.

It saw something pure white jutting out from the middle of its chest. At the same time, another fragment of bone had pierced its calf and lodged deep in the ground.

“Where do you think you’re going?”

With the Skeleton King’s voice sinking low, wind rushed in from behind.

Feeling the Skeleton King’s presence rapidly closing in, the Doppelganger gritted its teeth. The bone fragment pinning its calf to the ground was as solid as a stake.

*Crack!*

Though far below the Skeleton King, its new body was still strong enough to be called an A-rank Hunter.

The Doppelganger tore off its leg below the knee and moved its one remaining leg.

It gathered all its strength and kicked off the ground.

*BOOM!*

A deafening crash, and a fierce wind swept over its body.

The Doppelganger’s eyes burned with longing as it stared at the temple entrance, now right in front of it.

Just this once. If only it could get out of here.

If only it could somehow avoid Erasure…

*I swear, I’ll turn the world you tried to protect into ashes.*

And just as it reached out toward the secret door, open only to it—

*SHWEEEE!*

From somewhere far away—

*CRUNCH!*

A streak of light tore through space and swallowed the Doppelganger whole. It ripped and smashed it to pieces.

In the darkness that flooded its vision, someone’s voice pierced its ears.

“You fucking bastard. You invite a guest over and then try to leave?”

How cold that voice sounded.

And how hot the flames bursting from the spearhead buried in its body.

*Fwoosh.*

*ROOOAR!*

In a view dyed entirely blue and white, the Doppelganger writhed, engulfed in blue-white flames, unable even to scream.

Until the body that had once belonged to someone else burned to ash along with every last bit of its vitality.

Until, where all the lies it had piled up had burned away, only a single truth remained.

*Step. Step.*

*Whoosh.*

Wind swept through the unsteady footsteps, scattering the ash.

Among the ash that had settled in a thick layer, a black and ashen-white shadow stirred.

“…So that’s it.”

Jin Taekyung stood before it, supported by the Skeleton King. He looked down at the shadow with a faint light in his eyes.

The sole truth of a being built entirely from lies. He had pierced through to its pathetic essence.

> **System**
> **Level 10 Doppelganger**

“Turns out this is all you were.”

The shadow trembled—no, the Doppelganger trembled.

* * *

Just standing there was enough to leave me gasping.

As my senses slowly faded and my vision blurred, the pounding of my heart echoed like thunder.

*Thump. Thump-thump.*

Was this the price of pouring all my strength into that final strike?

My whole body trembled. If the Skeleton King hadn’t been supporting me, I would’ve collapsed long ago.

But I didn’t collapse.

Even now, I pushed back the sleep demon pressing in from every direction, pulled away from the Skeleton King’s support, and stood tall on my own two feet.

Then I looked down.

At a shadow as small as a child, yet made of an evil so pure it couldn’t be compared to any child’s.

At the hideous being that was now nothing more than a shadow.

“Yeah. This was all you were.”

I muttered the words I’d said earlier, almost to myself.

Looking at the Doppelganger trembling as if afraid, at the Level window floating over its head, I couldn’t help but feel a bitter laugh bubbling up.

> **System**
> **Level 10 Doppelganger**

Level 10.

That was all. Nothing more, nothing less.

For a Hunter, it was at the bottom of F-rank. For a Murim practitioner, it was about the level of a Third Rate swordsman who’d only just begun to sense internal energy.

That was the Doppelganger’s essence, confirmed by the *Eye of Truth*. Its origin, and the one and only truth.

*To think, a thing like this…*

I swallowed the words rising in me and clenched my teeth.

When I closed my eyes, flames flickered in the darkness.

A city in ruins.

Among the smoke rising from every corner, I saw bodies strewn about. The screams of those still alive echoed in my ears.

How many people had died because of the Doppelganger’s terrorist attacks, because of the monsters?

How many had lost their homes and had to say goodbye to their precious family and friends?

Hundreds of thousands? Millions?

I didn’t know.

More than thirty years had passed since the Doppelganger had slipped into this world. I couldn’t even begin to guess what it had done behind the scenes.

*Grind.*

My fists clenched tight.

I felt red drops of blood run between my nails, which had dug deep into my skin. I opened my eyes, but nothing had disappeared.

Not the ruined city. Not the emptiness in the dead people’s eyes or the cries of those still alive.

My mind remembered it all. It was branded into my eyes and ears, impossible to erase.

And the only thing among all of that, the only thing before my eyes, was this one being.

*Crush.*

“Ghk. Guhh…”

The energy in my foot crushed the shadow.

The Doppelganger, writhing and groaning, begged me for mercy. It could feel pain, even in this cursed form.

“S-save…”

“Save you?”

“Y-yes. Anything. I’ll do anything! I swear!”

I found myself staring down at it, momentarily dazed. Then I gathered the internal energy I had left and sent it surging through my foot.

*Crack. Crunch!*

“AAAGH!”

I just watched the Doppelganger scream.

Then the Skeleton King suddenly placed a hand on my shoulder.

“Human.”

“What?”

I’d only asked him a question, but when the Skeleton King met my gaze, he quietly moved his lips.

“…Nothing.”

What kind of expression did I have on my face right now? Was I tired and worn out? Or was my face twisted with a rage I’d never shown before?

It was probably the latter.

The Doppelganger had been writhing in pain, but when it saw my expression, it stopped screaming.

Then it said this in a voice filled with terror:

“I-I didn’t want to do it! Have you forgotten? It was all on the king’s orders!”

The king.

Demon King Asmodeus.

At the name that rose with its cry, the anger that had seized my body and mind wavered.
```
